from app.db.collections import users_collection
from app.schemas.user import UserOut

async def get_user_by_uid(uid: str) -> UserOut:
    doc = users_collection.document(uid).get()
    if doc.exists:
        return UserOut(**doc.to_dict())
    else:
        return None