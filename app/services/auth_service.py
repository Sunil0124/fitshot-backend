from fastapi import HTTPException, status
from passlib.context import CryptContext
from firebase_admin import auth as firebase_auth
from firebase_admin import firestore
import jwt, os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
db = firestore.client()

SECRET_KEY = os.getenv("JWT_SECRET", "your-secret")
ALGORITHM = "HS256"

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def register_user(user_data):
    try:
        user = firebase_auth.create_user(
            email=user_data.email,
            password=user_data.password,
            display_name=user_data.name
        )
        db.collection("users").document(user.uid).set({
            "email": user_data.email,
            "name": user_data.name,
            "uid": user.uid,
            "role": "student"
        })
        token = create_access_token({"uid": user.uid, "email": user_data.email})
        return token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def login_user(email, password):
    users = db.collection("users").where("email", "==", email).stream()
    user_doc = next(users, None)
    if not user_doc:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user_doc.to_dict()
    if not verify_password(password, user_data.get("hashed_password")):
        raise HTTPException(status_code=401, detail="Incorrect password")
    token = create_access_token({"uid": user_data["uid"], "email": email})
    return token


