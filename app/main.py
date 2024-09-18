from fastapi import FastAPI
from app.auth import router as auth_routes
from app.employees import router as employees_routes

app = FastAPI()

@app.get("/")
def read_root():
    """Root API"""
    return { "message": "API for Sprout Exam" }

app.include_router(auth_routes.router)
app.include_router(employees_routes.router)
