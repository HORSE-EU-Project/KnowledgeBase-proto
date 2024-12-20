from typing import Optional, List
from pydantic import BaseModel
from typing_extensions import TypedDict
from datetime import datetime

class Timeframe(TypedDict):
    start: datetime
    end: datetime

class Mitigation(BaseModel):
    mitigation_name: str

class MitigationPriority(BaseModel):
    name: str
    priority: int
    description: str

class MitigationFields(BaseModel):
    name: str
    value: str

class MitigationComplete(BaseModel):
    name: str
    priority: int
    fields: Optional[List[MitigationFields]] = None
    description: str

class Attack(BaseModel):
    attack_name: str
    mitigations: Optional[List[MitigationPriority]] = None

class AttackComplete(BaseModel):
    attack_name: str
    mitigations: Optional[List[MitigationComplete]] = None

class AttackList(BaseModel):
    attack_list: List[str]