from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_db
from models import User

router = APIRouter()

@router.get('/users')
async def get_all_users(db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@router.get('/users/{user_id}')
async def get_user(user_id: int, db: AsyncSession = Depends(get_async_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user

@router.post('/users')
async def create_user(name: str, email: str, db: AsyncSession = Depends(get_async_db)):
    existing = await db.execute(select(User).where(User.email == email))
    if existing.scalars().first():
        raise HTTPException(status_code=400, detail='Email already exists')
    user = User(name=name, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.get('/health')
async def health():
    return {'status': 'ok'}