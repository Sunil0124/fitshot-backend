rom pydantic import BaseModel

class TokenPayload(BaseModel):
    uid: str
    email: str
    name: str
    role: str