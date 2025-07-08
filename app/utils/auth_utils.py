from fastapi import Header, HTTPException, Depends
from app.services.auth_service import verify_firebase_token
from app.schemas.auth_schema import TokenPayload

async def get_current_user(authorization: str = Header(...)) -> TokenPayload:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")

    token = authorization.split(" ")[1]
    try:
        return await verify_firebase_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")