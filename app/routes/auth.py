from fastapi import APIRouter, Depends, HTTPException
from app.utils.auth_utils import get_current_user

router = APIRouter()

@router.get("/me")
async def get_me(current_user: dict = Depends(get_current_user)):
    return current_user


# app/routes/user.py
from fastapi import APIRouter, Depends
from app.utils.auth_utils import get_current_user

router = APIRouter()

@router.get("/profile")
async def get_user_profile(current_user: dict = Depends(get_current_user)):
    return {"message": "User profile fetched", "user": current_user}
