from fastapi import APIRouter, HTTPException
from app.schemas.theme import ThemeUpdate
from app.services.organization_service import update_org_theme

router = APIRouter()

@router.put("/themes/{org_id}", summary="Update organization theme")
async def update_theme(org_id: str, theme_data: ThemeUpdate):
    try:
        result = await update_org_theme(org_id, theme_data)
        return {"message": "Theme updated successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
