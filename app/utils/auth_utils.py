from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt, os

SECRET_KEY = os.getenv("JWT_SECRET", "your-secret")
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {
            "uid": payload.get("uid"),
            "email": payload.get("email"),
            "role": payload.get("role", "student"),
            "name": payload.get("name", "User")
        }
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )