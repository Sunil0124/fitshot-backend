from pydantic import BaseModel, EmailStr

class UserOut(BaseModel):
    uid: str
    name: str
    email: EmailStr
    role: str


# app/services/user_service.py
from app.db.firestore import db

async def get_user_by_id(uid: str):
    doc = db.collection("users").document(uid).get()
    if doc.exists:
        return doc.to_dict()
    return None