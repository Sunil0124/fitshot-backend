from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    uid: str
    name: str
    email: str
    role: str
    phone: Optional[str] = None
    status: Optional[str] = "active"

class UserOut(UserBase):
    pass