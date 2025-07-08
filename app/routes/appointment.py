from fastapi import APIRouter, Depends
from app.utils.auth_utils import get_current_user
from app.schemas.appointment import AppointmentCreate, AppointmentOut
from app.services.appointment_service import create_appointment, get_appointments_for_user
from typing import List

router = APIRouter()

@router.post("/", response_model=AppointmentOut)
async def create_new_appointment(data: AppointmentCreate, current_user: dict = Depends(get_current_user)):
    return await create_appointment(current_user["uid"], data)

@router.get("/me", response_model=List[AppointmentOut])
async def fetch_my_appointments(current_user: dict = Depends(get_current_user)):
    return await get_appointments_for_user(current_user["uid"])

