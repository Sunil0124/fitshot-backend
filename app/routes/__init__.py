from fastapi import APIRouter
from app.routes import auth, user, trainer, appointment, domain, organization, theme

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(trainer.router, prefix="/trainers", tags=["Trainers"])
api_router.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])
api_router.include_router(domain.router, prefix="/domains", tags=["Domains"])
api_router.include_router(organization.router, prefix="/organization", tags=["Organization"])
api_router.include_router(theme.router, prefix="/org", tags=["Themes"])
