from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    name: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"