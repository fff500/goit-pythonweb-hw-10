from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.auth import Hash
from src.schemas import UserCreate, UserModel
from src.services.users import UserService
from src.database.db import get_db


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user_service = UserService(db)

    user_by_email = await user_service.get_user_by_email(user_data.email)
    if user_by_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
        )

    user_by_username = await user_service.get_user_by_username(user_data.username)
    if user_by_username:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists",
        )

    user_data.password = Hash().get_password_hash(user_data.password)
    new_user = await user_service.create_user(user_data)
    return new_user
