"""Utility functions for token creation and verification."""
from datetime import datetime, timedelta, timezone
from typing import Union
from pydantic import BaseModel
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from .services import get_user_by_username
from app.database import get_db
from app.auth import services
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """Create access token with data and expiration time."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """Verify token and return token data."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return False
        return TokenData(username=username)
    except JWTError:
        return False

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    """Get the currently authenticated user from the token."""
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token)
    if not token_data:
        raise credentials_exception
    user = await services.get_user_by_username(token_data.username, db)
    if not user:
        raise credentials_exception
    return user
