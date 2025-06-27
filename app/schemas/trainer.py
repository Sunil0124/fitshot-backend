from pydantic import BaseModel

class TrainerCreate(BaseModel):
    name: str
    email: str
    domain: str

class TrainerOut(TrainerCreate):
    id: str
