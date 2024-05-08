from typing import Optional, List
from typing_extensions import TypedDict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, networks
from datetime import datetime

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

import logging

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

class AttackList(BaseModel):
    attack_list : List[str]

def get_all_attacks() -> List[str]:
    # create connection with database
    engine = create_engine('postgresql+psycopg2://postgres:md5579e4@attacks-mitigations-database:5432/knowledge-base') # TODO remove password
    conn = engine.connect()

    try:
        query = text(f"SELECT name FROM attack;")
        attacks_list = conn.execute(query)
        attacks_list = attacks_list.fetchall()
        if not attacks_list:
            raise HTTPException(status_code=404, detail=f"There exists no attacks in the database")

        # commit the transaction
        conn.commit()

        # extract the results
        results = [attacks[0] for attacks in attacks_list]
        logger = logging.getLogger("mycoolapp")
        logger.error("1-------->")
        logger.error(results)
        return results
    
    except OperationalError as e:
        # If there's an operational error, raise it
        raise e

    finally:
        # Close the connection
        conn.close()


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
    # create connection with database
    engine = create_engine('postgresql+psycopg2://postgres:md5579e4@attacks-mitigations-database:5432/knowledge-base') # TODO remove password
    conn = engine.connect()

    try:
        # execute query
        query = text(f"SELECT mitigation FROM attack WHERE name = '{attack}';")   # check security issues
        mitigations = conn.execute(query)
        mitigations = mitigations.fetchall()
        if not mitigations:
            raise HTTPException(status_code=404, detail=f"There exists no mitigation associated to attack '{attack}'")

        # commit the transaction
        conn.commit()

        # extract results
        results = [mitigation[0] for mitigation in mitigations]
        return results

    except OperationalError as e:
        # If there's an operational error, raise it
        raise e

    finally:
        # Close the connection
        conn.close()


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
    # create connection with database
    engine = create_engine('postgresql+psycopg2://postgres:md5579e4@attacks-mitigations-database:5432/knowledge-base') # TODO remove password
    conn = engine.connect()

    try:
        # execute query
        query = text(f"SELECT playbook_endpoint FROM mitigation WHERE name = '{mitigation}';")
        playbook = conn.execute(query).fetchall()

        # commit the transaction
        conn.commit()

        # check if there are no results
        if not playbook:
            raise HTTPException(status_code=404, detail=f"There exists no playbook endpoint associated to mitigation '{mitigation}'")

        # extract playbook endpoint
        playbook_endpoint = playbook[0][0]
        return playbook_endpoint

    except OperationalError as e:
        # If there's an operational error, raise it
        raise e

    finally:
        # Close the connection
        conn.close()

app = FastAPI()

@app.post("/mitigations")
def fetch_mitigation(attack: Attack) -> Attack:
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
def fetch_playbook(mitigation: Mitigation) -> Playbook:
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

@app.get("/allattacks")
def get_all_attacks() -> AttackList:
    """
    Retrieves a list of all attacks from the database.

    Returns:
        AttackList: An object containing a list of all attacks retrieved from the database.
    
    Raises:
        HTTPException: If there are no attacks in the database.
        OperationalError: If there is an operational error while connecting to the database.
    """
    # create connection with database
    engine = create_engine('postgresql+psycopg2://postgres:md5579e4@attacks-mitigations-database:5432/knowledge-base') # TODO remove password
    conn = engine.connect()

    try:
        query = text(f"SELECT DISTINCT name FROM attack;")
        attacks_list = conn.execute(query)
        attacks_list = attacks_list.fetchall()
        if not attacks_list:
            raise HTTPException(status_code=404, detail=f"There exists no attacks in the database")

        # commit the transaction
        conn.commit()

        # extract the results
        attack_list = [attacks[0] for attacks in attacks_list]
        response = AttackList(attack_list=attack_list)  
        return response
    
    except OperationalError as e:
        # If there's an operational error, raise it
        raise e

    finally:
        # Close the connection
        conn.close()
      