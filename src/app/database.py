from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException
from typing import List
import os
from dotenv import load_dotenv
import logging
from src.app.models import MitigationPriority, MitigationFields, MitigationComplete

load_dotenv()

DB_SECRET = os.getenv('DB_SECRET')
DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')

def get_engine():
    return create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_SECRET}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}')

def get_all_attacks() -> List[str]:
    """
    Retrieves all attack names from the database.

    Returns:
        List[str]: A list of attack names.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there are no attacks in the database.
    """
    engine = get_engine()
    conn = engine.connect()
    try:
        query = text("SELECT name FROM attack;")
        attacks_list = conn.execute(query).fetchall()
        if not attacks_list:
            raise HTTPException(status_code=404, detail="There exists no attacks in the database")
        conn.commit()
        results = [attacks[0] for attacks in attacks_list]
        return results
    except OperationalError as e:
        raise e
    finally:
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
    engine = get_engine()
    conn = engine.connect()
    try:
        query = text(f"SELECT mitigation, mitigation_priority, description FROM attacks_mitigations WHERE attack = '{attack}' ORDER BY mitigation_priority;")
        mitigations = conn.execute(query).fetchall()
        if not mitigations:
            raise HTTPException(status_code=404, detail=f"There exists no mitigation associated to attack '{attack}'")
        conn.commit()
        mitigations_list = [MitigationPriority(name=mitigation[0], priority=mitigation[1], description=mitigation[2]) for mitigation in mitigations]
        return mitigations_list
    except OperationalError as e:
        raise e
    finally:
        conn.close()

def get_mitigation(attack: str) -> List[str]:
    """
    Retrieves detailed mitigation measures associated with a specific attack from the database.

    Parameters:
        attack (str): The name of the attack for which to retrieve detailed mitigation measures.

    Returns:
        List[MitigationComplete]: A list of detailed mitigation measures with their priorities, fields, and description associated with the specified attack.

    Raises:
        sqlalchemy.exc.OperationalError: If there is an operational error while connecting to the database.
        fastapi.HTTPException: If there are no detailed mitigation measures associated with the specified attack.
    """
    engine = get_engine()
    conn = engine.connect()
    try:
        query = text(f"SELECT mitigation, mitigation_priority, array_agg(field_name) as field_names, array_agg(field_value) AS field_values, description FROM attacks_mitigations AS am INNER JOIN mitigation AS m ON am.mitigation = m.name WHERE attack = '{attack}' GROUP BY mitigation, mitigation_priority, description ORDER BY mitigation_priority;")
        mitigations = conn.execute(query).fetchall()
        if not mitigations:
            raise HTTPException(status_code=404, detail=f"There exists no mitigation associated to attack '{attack}'")
        conn.commit()
        mitigations_list = []
        for mitigation in mitigations:
            if all(item is None for item in mitigation[2]) and all(item is None for item in mitigation[3]):
                mitigation_fields = None  
            else:  
                mitigation_fields = [
                    MitigationFields(name=name if name is not None else "", value=value if value is not None else "")
                    for name, value in zip(mitigation[2], mitigation[3])
                ]
            if mitigation_fields is None:
                mitigation_priority = MitigationComplete(name=mitigation[0], priority=mitigation[1], description=mitigation[4])
            else:
                mitigation_priority = MitigationComplete(name=mitigation[0], priority=mitigation[1], fields=mitigation_fields, description=mitigation[4])
            mitigations_list.append(mitigation_priority.dict(exclude_none=True))
        return mitigations_list
    except OperationalError as e:
        raise e
    finally:
        conn.close()