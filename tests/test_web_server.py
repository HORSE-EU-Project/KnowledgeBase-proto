import sys
from os.path import abspath, dirname
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException



sys.path.insert(0, dirname(abspath(__file__)))

from src.app.main import hello_world, get_all_attacks, get_mitigation

## variables
N_ATTACKS_IN_DB = 3

def test_hello_world():
    assert hello_world() == "hello world"

def test_get_all_attacks():
    assert get_all_attacks() is not None
    assert len(get_all_attacks().attack_list) == N_ATTACKS_IN_DB
    assert 'ntp_dos' in get_all_attacks().attack_list

def test_get_mitigation():
    try:
        get_mitigation('wrong_input')
        assert False
    except HTTPException:
        assert True
    assert get_mitigation('ntp_dos') is not None
    assert len(get_mitigation('pfcf_dos')) > 1
    assert get_mitigation('dns_reflection_amplification')[0].name == 'dns_service_disable'