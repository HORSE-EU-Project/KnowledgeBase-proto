from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

# vars
N_ATTACKS = 3       

def test_hello_world():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == "hello world"

def test_all_attacks():
    response = client.get("/allattacks")
    assert response.status_code == 200
    assert "attack_list" in response.json()
    assert len(response.json()["attack_list"]) == N_ATTACKS

def test_fetch_mitigations():
    response = client.post("/mitigations", json={"attack_name": "pfcf_dos"})
    assert response.status_code == 200
    assert all(key in response.json() for key in ["attack_name", "mitigations"])
    assert len(response.json()["mitigations"]) > 1
    assert all(key in response.json()["mitigations"][0] for key in ["name", "priority", "description"])
    # test errors here