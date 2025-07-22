from fastapi import APIRouter, HTTPException
from app.schemas.organization import OrganizationCreate, OrganizationOut, OrganizationUpdate
from app.services.organization_service import create_organization, update_organization

router = APIRouter(tags=["Organization"])

@router.post("/", response_model=OrganizationOut)
async def create_org(data: OrganizationCreate):
    org = await create_organization(data.dict())
    return org

@router.put("/{org_id}", response_model=OrganizationOut)
async def update_org(org_id: str, data: OrganizationUpdate):
    updated = await update_organization(org_id, data.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Organization not found")
    return updated
