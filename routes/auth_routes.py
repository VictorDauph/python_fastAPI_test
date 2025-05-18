from fastapi import APIRouter

from controllers.auth_controller import register, login
from schemas_validators.user_schema import UserResponse, UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
async def register_user_route(user:UserCreate):
    try:
        new_user:UserResponse= await register(user)
        return new_user
    except Exception as e:
        return {"error":str(e)}

@router.post("/login")
async def login_route(user:UserCreate):
    try:
        return await login(user)
    except Exception as e:
        return {"error":str(e)}