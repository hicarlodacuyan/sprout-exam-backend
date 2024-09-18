"""This module contains the business logic for the auth service"""

from passlib.context import CryptContext
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(username: str, password: str, db: AsyncSession):
    """Create a new user"""
    hashed_password = pwd_context.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    db.add(user)
    await db.commit()
    return {"username": user.username}

async def authenticate_user(username: str, password: str, db: AsyncSession):
    """Authenticate a user"""
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    user = result.scalars().first()

    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

async def get_user_by_username(username: str, db: AsyncSession):
    """Get a user by their username"""
    query = select(User).where(User.username == username)
    result = await db.execute(query)
    user = result.scalars().first()
    return user
