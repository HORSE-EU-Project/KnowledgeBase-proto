from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

# variables
N_ATTACKS = 14      

def test_hello_world():

    endpoint = "/helloworld"

    # Test a generic GET to the server
    response = client.get(endpoint)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the request correctly returns an 'hello world
    assert response.json() == "hello world"


def test_all_attacks():

    endpoint = "/allattacks"

    # Test GET allattacks
    response = client.get(endpoint)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response json contains the field 'attack_list'
    assert "attack_list" in response.json()

    # Assert that the length of attacks returned is equal to the number of attacks expected in the db
    assert len(response.json()["attack_list"]) == N_ATTACKS


def test_fetch_mitigations():

    endpoint = "/mitigations_restricted"
    json = {
        "attack_name": "pfcf_dos"
        }

    # Test POST to retrieve mitigations given 'pfcf_dos' as attack input
    response = client.post(endpoint, json=json)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response json contains the fields 'attack_name' and 'mitiagions'
    assert all(key in response.json() for key in ["attack_name", "mitigations"])

    # Assert that the response json mitigations is an object of length > 1
    assert len(response.json()["mitigations"]) > 1

    # Assert that the first element of mitigations list is an object containing the fields 'name', 'priority', 'description'
    assert all(key in response.json()["mitigations"][0] for key in ["name", "priority", "fields", "description"])

def test_fetch_mitigations_unknown_attack():
    endpoint = "/mitigations_restricted"
    json = {
        "attack_name" : "unknown_attack_name"
    }

    # Test POST to retrieve mitigations given an unknown attack name
    response = client.post(endpoint, json=json)

    # Assert that the response status code is 404 (Not Found)
    assert response.status_code == 404

def test_fetch_mitigations_wrong_json():
    endpoint = "/mitigations_restricted"
    json = {
        "no_attack_name" : "pfcf_dos"
    }

    # Test POST to retrieve mitigations with no attack_name field in the json body
    response = client.post(endpoint, json=json)

    # Assert that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422

