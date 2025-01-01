from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, planner
from app import models

# Create the FastAPI app
app = FastAPI(
    title="Weekly Planner",
    description="A simple weekly planner with authentication and authorization.",
    version="1.0.0"
)

# Automatically create tables if they do not exist
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(planner.router, prefix="/planner", tags=["Planner"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Weekly Planner API!"}
