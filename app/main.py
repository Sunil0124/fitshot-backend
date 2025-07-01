from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import api_router
import app.utils.firebase  # triggers Firebase init

app = FastAPI(
    title="Fitshot API",
    version="1.0.0",
    description="Backend API for Fitshot - fitness training and appointment app"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all routes
app.include_router(api_router)