from typing import Union, Optional, List
from typing_extensions import TypedDict

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, networks
from datetime import datetime

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import json

class Playbook(BaseModel):
    mitigation : str
    url : networks.Url

class Threat(TypedDict):
    type: str
    service: str
    port: List[int]


class Timeframe(TypedDict):
    start: datetime
    end: datetime

class Mitigation(BaseModel):
    mitigation_name : str

class Attack(BaseModel):
    subnet_address: str  # ip address?
    threat: Threat
    time_frame: Timeframe
    mitigation : Optional[List[int]] = None

def get_mitigation(attack: str) -> List[str]:
    """
    Retrieves mitigation measures associated with a specific attack from the database.

    Parameters:
        attack (str): The name of the attack for which to retrieve mitigation measures.

    Returns:
        List[str]: A list of mitigation measures associated with the specified attack.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there are no mitigation measures associated with the specified attack.
    """
    
    results = ['filter_network_traffic', 'mitigation_2']

    return results


def get_playbook(mitigation: str) -> str:
    """
    Retrieves the playbook endpoint associated with a specific mitigation measure from the database.

    Parameters:
        mitigation (str): The name of the mitigation measure for which to retrieve the playbook endpoint.

    Returns:
        str: The playbook endpoint associated with the specified mitigation measure.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there is no playbook endpoint associated with the specified mitigation measure.
    """
    playbook_endpoint = "https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html"
    return playbook_endpoint

app = FastAPI()

@app.post("/mitigations")
async def fetch_mitigation(attack: Attack) -> Attack:
    """
    Fetches mitigation measures for a given attack.

    Parameters:
        attack (Attack): An object containing information about the attack.

    Returns:
        Attack: The response contains the same Attack object with the mitigation attribute populated.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there are no mitigation measures associated with the specified attack.
    """
    attack.mitigation = get_mitigation(attack.threat["type"])
    response = attack
    return response

@app.post("/playbooks")
async def fetch_playbook(mitigation: Mitigation) -> Playbook:
    """
    Fetches the playbook URL associated with a mitigation measure.

    Parameters:
        mitigation (Mitigation): An object containing the name of the mitigation measure.

    Returns:
        Playbook: A Playbook object containing the mitigation name and playbook URL.

    Raises:
        HTTPException: If there is no playbook endpoint associated with the specified mitigation measure.
    """
    try:
        playbook_url = get_playbook(mitigation.mitigation_name)
        response = Playbook(mitigation=mitigation.mitigation_name, url=playbook_url)
        return response

    except HTTPException as e:
        # If there's an HTTPException, re-raise it
        raise e