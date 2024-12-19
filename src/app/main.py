from typing import Optional, List
from typing_extensions import TypedDict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, networks
from datetime import datetime

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

import logging
import os
from dotenv import load_dotenv

class Timeframe(TypedDict):
    start: datetime
    end: datetime

class Mitigation(BaseModel):
    mitigation_name : str


class MitigationPriority(BaseModel):
    name : str
    priority : int
    description : str

class MitigationFields(BaseModel):
    name : str
    value : str

class MitigationComplete(BaseModel):
    name : str
    priority : int
    fields : Optional[List[MitigationFields]] = None
    description : str

class Attack(BaseModel):
    attack_name : str
    mitigations : Optional[List[MitigationPriority]] = None

class AttackComplete(BaseModel):
    attack_name : str
    mitigations : Optional[List[MitigationComplete]] = None

class AttackList(BaseModel):
    attack_list : List[str]

# load env variables
load_dotenv()

DB_SECRET = os.getenv('DB_SECRET')
DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')

def get_all_attacks() -> List[str]:
    # create connection with database
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_SECRET}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}')
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


def get_mitigation_restricted(attack: str) -> List[str]:
    """
    Retrieves mitigation measures associated with a specific attack from the database.

    Parameters:
        attack (str): The name of the attack for which to retrieve mitigation measures.

    Returns:
        List[MitigationPriority]: A list of mitigation measures with their priorities and description associated with the specified attack.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there are no mitigation measures associated with the specified attack.
    """
    # create connection with database
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_SECRET}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}')

    conn = engine.connect()
    
    try:
        # execute query
        query = text(f"SELECT mitigation, mitigation_priority, description FROM attacks_mitigations WHERE attack = '{attack}' ORDER BY mitigation_priority;")   # check security issues
        mitigations = conn.execute(query)
        mitigations = mitigations.fetchall()
        if not mitigations:
            raise HTTPException(status_code=404, detail=f"There exists no mitigation associated to attack '{attack}'")

        # commit the transaction
        conn.commit()

        logger = logging.getLogger("mycoolapp")
        logger.error(f"LOG: {mitigations} ")

        # extract results
        mitigations_list = []
        
        for mitigation in mitigations:
            mitigation_priority = MitigationPriority(name=mitigation[0], priority=mitigation[1], description=mitigation[2])
            mitigations_list.append(mitigation_priority)
        
        results = mitigations_list
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
        List[MitigationPriority]: A list of mitigation measures with their priorities and description associated with the specified attack.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there are no mitigation measures associated with the specified attack.
    """
    # create connection with database
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_SECRET}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}')

    conn = engine.connect()
    
    try:
        # execute query
        query = text(f"SELECT mitigation, mitigation_priority, array_agg(field_name) as field_names, array_agg(field_value) AS field_values, description FROM attacks_mitigations AS am INNER JOIN mitigation AS m ON am.mitigation = m.name WHERE attack = '{attack}' GROUP BY mitigation, mitigation_priority, description ORDER BY mitigation_priority;")   # check security issues

        mitigations = conn.execute(query)
        mitigations = mitigations.fetchall()
        if not mitigations:
            raise HTTPException(status_code=404, detail=f"There exists no mitigation associated to attack '{attack}'")

        # commit the transaction
        conn.commit()

        # extract results
        mitigations_list = []
        
        for mitigation in mitigations:
            if all(item is None for item in mitigation[2]) and all(item is None for item in mitigation[3]):
                mitigation_fields = None  
            else:  
                mitigation_fields = [
                    MitigationFields(name=name if name is not None else "", value=value if value is not None else "")
                    for name, value in zip(mitigation[2], mitigation[3])
                ]

            # Only include 'fields' if it's not None
            if mitigation_fields is None:
                mitigation_priority = MitigationComplete(name=mitigation[0], priority=mitigation[1], description=mitigation[4])
            else:
                mitigation_priority = MitigationComplete(name=mitigation[0], priority=mitigation[1], fields=mitigation_fields, description=mitigation[4])

            mitigations_list.append(mitigation_priority.dict(exclude_none=True))
        
        results = mitigations_list
        return results

    except OperationalError as e:
        # If there's an operational error, raise it
        raise e

    finally:
        # Close the connection
        conn.close()

app = FastAPI()

@app.post("/mitigations_restricted")
def fetch_mitigation_restricted(attack: Attack) -> Attack:
    """
    Fetches mitigation measures for a given attack (restricted version).

    Parameters:
        attack (Attack): An object containing information about the attack.

    Returns:
        Attack: The response contains the same Attack object with the mitigation attribute populated.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there are no mitigation measures associated with the specified attack.
    """
    attack.mitigations = get_mitigation_restricted(attack.attack_name)
    response = attack
    return response


@app.post("/mitigations")
def fetch_mitigation(attack: AttackComplete) -> AttackComplete:
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
    attack.mitigations = get_mitigation(attack.attack_name)
    response = attack
    return response

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
    engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_SECRET}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}')
    
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

@app.get("/helloworld")
def hello_world():
    # example log
    logger = logging.getLogger("mycoolapp")
    logger.error("1-------->")
    return "hello world"
      