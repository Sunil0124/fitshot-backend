from pydantic import BaseModel
from typing import Optional

class Trainer(BaseModel):
    id: str
    user_id: str  # Firebase UID
    expertise: str
    bio: Optional[str] = None
    available: bool = True
