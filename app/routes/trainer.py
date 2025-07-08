from fastapi import APIRouter, Depends
from app.utils.auth_utils import get_current_user

router = APIRouter()

@router.get("/")
async def list_trainers(current_user: dict = Depends(get_current_user)):
    return {"message": "List of trainers"}
