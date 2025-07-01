from app.db.collections import appointments_collection
from app.schemas.appointment import AppointmentCreate, AppointmentOut
from datetime import datetime
import uuid

async def create_appointment(user_id: str, data: AppointmentCreate) -> AppointmentOut:
    doc_id = str(uuid.uuid4())
    appointment = {
        "id": doc_id,
        "trainer_id": data.trainer_id,
        "user_id": user_id,
        "start_time": data.start_time,
        "end_time": data.end_time,
        "notes": data.notes,
        "status": "pending",
        "created_at": datetime.utcnow().isoformat(),
    }
    appointments_collection.document(doc_id).set(appointment)
    return AppointmentOut(**appointment)

async def get_appointments_for_user(user_id: str):
    docs = appointments_collection.where("user_id", "==", user_id).stream()
    return [doc.to_dict() for doc in docs]
