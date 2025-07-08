from firebase_admin import auth
from app.schemas.auth_schema import TokenPayload

async def verify_firebase_token(token: str) -> TokenPayload:
    try:
        decoded_token = auth.verify_id_token(token)
        return TokenPayload(
            uid=decoded_token["uid"],
            email=decoded_token.get("email", ""),
            name=decoded_token.get("name", ""),
            role=decoded_token.get("role", "athlete")  # Default to athlete
        )
    except Exception as e:
        raise ValueError("Invalid Firebase token")
