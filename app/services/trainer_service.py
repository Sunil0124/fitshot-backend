from app.db.collections import trainers_collection
from app.schemas.trainer import TrainerOut

async def list_trainers():
    docs = trainers_collection.stream()
    return [TrainerOut(**doc.to_dict()) for doc in docs]
