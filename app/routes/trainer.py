from fastapi import APIRouter, HTTPException
from app.schemas.trainer import TrainerCreate, TrainerOut
from app.services.trainer_service import create_trainer, get_all_trainers

router = APIRouter()

@router.post("/", response_model=TrainerOut)
async def register_trainer(trainer: TrainerCreate):
    return await create_trainer(trainer)

@router.get("/", response_model=list[TrainerOut])
async def fetch_trainers():
    return await get_all_trainers()
