from fastapi.openapi.models import Response
from starlette.responses import JSONResponse

from beanie_models.user_model import User
from repositories.user_repo import create_user_repo, get_user_by_username
from schemas_validators.user_schema import UserCreate, UserResponse, Token
from utils.jwt import create_access_token
from utils.password import hash_password


async def register(user:UserCreate)->UserResponse:
    hashed_password= hash_password(user.password)
    new_user:User = await create_user_repo(user,hashed_password)
    return UserResponse(
        username=new_user.username,
        id=new_user.id
    )

async def login(user:UserCreate)->Response:
    user = await get_user_by_username(user.username)
    if user:
       user_string = user.model_dump(include={"id", "username"})
       user_string["id"] = str(user_string["id"])
       token:str = create_access_token(user_string)
       response = JSONResponse(content={"message": "Connexion réussie"})
       response.set_cookie(
           key="access_token",
           value=token,
           httponly=True,
           secure=False,  # À mettre à False en local sans HTTPS
           samesite="lax",  # Ou "lax" selon ton usage
           max_age=3600,  # Durée de vie en secondes
           path="/"
       )
       return response
    raise Exception("User not found")
