from beanie import Document, PydanticObjectId, Indexed
from pydantic import Field
from typing import Optional

from schemas_validators.user_schema import UserCreate


class User(Document):
    username: Indexed(str, unique=True) = Field(..., description="Nom d'utilisateur unique")
    hashed_password: str

    class Settings:
        name = "users"  # nom de la collection MongoDB
