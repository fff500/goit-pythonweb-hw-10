from fastapi import APIRouter, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.schemas import UserModel
from src.services.auth import get_current_user


router = APIRouter(prefix="/users", tags=["users"])
limiter = Limiter(key_func=get_remote_address)


@router.get(
    "/me", response_model=UserModel, description="No more than 2 requests per minute"
)
@limiter.limit("2/minute")
async def me(request: Request, user: UserModel = Depends(get_current_user)):
    return user
