from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserOut
from app.services.user_service import get_user_by_id
from app.utils.auth_utils import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserOut)
async def read_users_me(current_user: UserOut = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
