from fastapi import FastAPI
from app.auth import router as auth_routes
from app.employees import router as employees_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can set it to ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods: GET, POST, etc.
    allow_headers=["*"],  # Allow all headers (like Authorization, Content-Type)
)

@app.get("/")
def read_root():
    """Root API"""
    return { "message": "API for Sprout Exam" }

app.include_router(auth_routes.router)
app.include_router(employees_routes.router)
