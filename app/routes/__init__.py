from fastapi import APIRouter
from app.routes import auth, user, trainer, appointment, domain

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(user.router, prefix="/users", tags=["Users"])
api_router.include_router(trainer.router, prefix="/trainers", tags=["Trainers"])
api_router.include_router(appointment.router, prefix="/appointments", tags=["Appointments"])
api_router.include_router(domain.router, prefix="/domains", tags=["Domains"])


# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from app.utils.auth_utils import get_current_user

router = APIRouter()