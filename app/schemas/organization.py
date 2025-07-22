from pydantic import BaseModel, EmailStr
from typing import Optional, Dict


class OrganizationCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    domain: str  # e.g., student, trainer
    theme: Optional[Dict[str, str]] = None


class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    domain: Optional[str] = None
    theme: Optional[Dict[str, str]] = None


class OrganizationOut(BaseModel):
    id: str
    name: str
    email: EmailStr
    domain: str

    model_config = {
        "from_attributes": True
    }

class OrganizationWithTheme(OrganizationOut):
    theme: Optional[Dict[str, str]] = None
