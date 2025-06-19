from fastapi import APIRouter, Depends

from src.schemas import UserModel
from src.services.auth import get_current_user


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserModel)
async def me(user: UserModel = Depends(get_current_user)):
    return user
