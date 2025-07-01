from pydantic import BaseModel

class DomainOut(BaseModel):
    id: str
    name: str