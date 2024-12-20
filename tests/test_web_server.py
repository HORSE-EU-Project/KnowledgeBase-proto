import sys
from os.path import abspath, dirname
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException

sys.path.insert(0, dirname(abspath(__file__)))

from src.app.database import get_mitigation_restricted
from src.app.routes import hello_world, fetch_all_attacks

# variables
N_ATTACKS_IN_DB = 3

def test_hello_world():
    assert hello_world() == "hello world"

def test_get_all_attacks():

    # Assert that the function returns any response
    assert fetch_all_attacks() is not None

    # Assert that the response has the n. of attacks expected from the db
    assert len(fetch_all_attacks().attack_list) == N_ATTACKS_IN_DB

    # Assert that ntp_dos is one of the attacks in the db
    assert 'ntp_dos' in fetch_all_attacks().attack_list

def test_get_mitigation():

    # Assert that giving a wrong input, the function throws an HttpException
    try:
        get_mitigation_restricted('wrong_input')
        assert False
    except HTTPException:
        assert True

    # Assert that giving a right input (ntp_dos) the function returns something
    assert get_mitigation_restricted('ntp_dos') is not None

    # Assert that the function returns an object with length > 1
    assert len(get_mitigation_restricted('pfcf_dos')) > 1

    # Assert that the name of the first mitigation to 'dns_reflection_amplification' is 'dns_service_disable' 
    assert get_mitigation_restricted('dns_reflection_amplification')[0].name == 'dns_service_disable'