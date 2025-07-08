from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Appointment(BaseModel):
    id: str
    trainer_id: str
    user_id: str
    start_time: datetime
    end_time: datetime
    status: str = "pending"
    notes: Optional[str] = None