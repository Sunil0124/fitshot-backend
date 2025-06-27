from app.schemas.trainer import TrainerCreate
from app.utils.firebase_ops import db

async def create_trainer(trainer: TrainerCreate):
    trainer_dict = trainer.dict()
    doc_ref = db.collection("trainers").add(trainer_dict)
    trainer_dict["id"] = doc_ref[1].id
    return trainer_dict

async def get_all_trainers():
    docs = db.collection("trainers").stream()
    return [{"id": doc.id, **doc.to_dict()} for doc in docs]
