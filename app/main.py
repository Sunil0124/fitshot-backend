from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, trainer, domain, appointment

app = FastAPI(
    title="Fitshot API",
    version="1.0.0",
    description="Backend API for Fitshot mobile and web apps."
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registration
app.include_router(auth.router, prefix="/api/auth")
app.include_router(trainer.router, prefix="/api/trainers")
app.include_router(domain.router, prefix="/api/domains")
app.include_router(appointment.router, prefix="/api/appointments")

@app.get("/")
def root():
    return {"message": "Fitshot API is running"}
