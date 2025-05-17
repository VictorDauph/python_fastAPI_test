from beanie import PydanticObjectId
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str =Field(..., min_length=3, example="user")
    password: str= Field(...,min_length=3, example="pwd")

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id:PydanticObjectId
    username: str