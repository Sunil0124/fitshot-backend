from pydantic import BaseModel
from typing import Optional

class TrainerBase(BaseModel):
    user_id: str
    expertise: str
    bio: Optional[str] = None
    available: bool = True

class TrainerOut(TrainerBase):
    id: str