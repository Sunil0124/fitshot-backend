from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "Domain route is working"}

@router.get("/")
async def list_domains():
    return ["health", "fitness", "strength"]

