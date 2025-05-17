from beanie_models.user_model import User
from repositories.user_repo import create_user_repo
from schemas_validators.user_schema import UserCreate, UserResponse
from utils.password import hash_password


async def register(user:UserCreate)->UserResponse:
    hashed_password= hash_password(user.password)
    new_user:User = await create_user_repo(user,hashed_password)
    return UserResponse(
        username=new_user.username,
        id=new_user.id
    )
