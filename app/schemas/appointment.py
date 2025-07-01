from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.enums import AppointmentStatus

class AppointmentCreate(BaseModel):
    trainer_id: str
    start_time: datetime
    end_time: datetime
    notes: Optional[str] = None

class AppointmentOut(AppointmentCreate):
    id: str
    user_id: str
    status: AppointmentStatus

