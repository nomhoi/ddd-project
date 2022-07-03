from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from application.adapters.database import get_db
from application.adapters.repositories.users import UserRepository
from application.domain.model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(prefix='/api', tags=['Users'])


@router.post("/users/")
async def create_user(username: str, email: str, db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    user = await user_repo.add(
        User(
            id=None,
            username=username,
            email=email
        )
    )
    return user


@router.get("/users/")
async def read_users(db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    users = await user_repo.list()
    return users


@router.get("/users/{id}")
async def read_user(id: int, db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    user = await user_repo.get(id=id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user