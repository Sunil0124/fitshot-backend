from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    uid: str
    name: str
    email: str
    role: str
    phone: Optional[str] = None
    status: Optional[str] = "active"