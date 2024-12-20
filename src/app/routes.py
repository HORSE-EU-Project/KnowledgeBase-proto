from fastapi import APIRouter
from src.app.models import Attack, AttackComplete, AttackList
from src.app.database import get_all_attacks, get_mitigation_restricted, get_mitigation

router = APIRouter()

@router.post("/mitigations_restricted")
def fetch_mitigation_restricted(attack: Attack) -> Attack:
    attack.mitigations = get_mitigation_restricted(attack.attack_name)
    return attack

@router.post("/mitigations")
def fetch_mitigation(attack: AttackComplete) -> AttackComplete:
    attack.mitigations = get_mitigation(attack.attack_name)
    return attack

@router.get("/allattacks")
def fetch_all_attacks() -> AttackList:
    attack_list = get_all_attacks()
    return AttackList(attack_list=attack_list)

@router.get("/helloworld")
def hello_world():
    return "hello world"