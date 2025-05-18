from beanie import PydanticObjectId
from fastapi import Request, HTTPException
from jose import JWTError

from repositories.user_repo import get_user_by_id
from utils import jwt


async def get_current_user(request:Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        payload= jwt.verify_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Token invalide")
        user_id = payload["id"]
        if not user_id:
            raise HTTPException(status_code=401, detail="Token invalide")
        user =await get_user_by_id(PydanticObjectId(user_id))
        if not user:
            raise HTTPException(status_code=401, detail="Utilisateur inconnu")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide")