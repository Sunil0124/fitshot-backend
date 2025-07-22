from typing import Dict
from uuid import uuid4
from app.db.collections import orgs_collection
from app.schemas.theme import ThemeUpdate
from app.utils.security import hash_password


async def create_organization(data: Dict):
    org_id = str(uuid4())
    org_data = {
        "id": org_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "password": hash_password(data.get("password")), 
        "domain": data.get("domain"),
        "theme": data.get("theme", {})
    }
    orgs_collection.document(org_id).set(org_data)
    return org_data


async def update_organization(org_id: str, updates: Dict):
    doc_ref = orgs_collection.document(org_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise ValueError(f"Organization with ID {org_id} not found")
    doc_ref.update(updates)
    return doc_ref.get().to_dict()


async def update_org_theme(org_id: str, theme_data: ThemeUpdate):
    theme_dict = theme_data.dict(exclude_unset=True)
    if not theme_dict:
        raise ValueError("No theme data provided")

    doc_ref = orgs_collection.document(org_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise ValueError("Organization not found")

    doc_ref.update({"theme": theme_dict})
    return theme_dict
