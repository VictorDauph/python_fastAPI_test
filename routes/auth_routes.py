from fastapi import APIRouter

from controllers.auth_controller import register
from schemas_validators.user_schema import UserResponse, UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
async def register_user_route(user:UserCreate):
    new_user:UserResponse= await register(user)
    return new_user