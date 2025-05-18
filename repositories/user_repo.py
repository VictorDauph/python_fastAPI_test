from typing import Any, Coroutine

from beanie_models.user_model import User
from schemas_validators.user_schema import UserCreate


async def create_user_repo(user:UserCreate,hashed_password:str)->User:
    new_user = User(username=user.username ,hashed_password=hashed_password)
    await new_user.insert()
    return new_user

async def get_user_by_username(username:str)-> User | None:
    user = await User.find_one(User.username == username)
    if user:
        return user
    return None