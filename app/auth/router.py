"""Auth routes module"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth import schemas, services, utils
from app.database import get_db

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/login", response_model=utils.Token)
async def login(
    user: schemas.UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """Login a user"""
    if not await services.authenticate_user(user.username, user.password, db):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = utils.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
async def register(
    user: schemas.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """Register a new user"""
    return await services.create_user(user.username, user.password, db)
