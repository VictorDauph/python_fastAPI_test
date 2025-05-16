from beanie import Document, PydanticObjectId
from pydantic import Field
from typing import Optional


class Produit(Document):
    nom: str
    prix: float

    class Settings:
        name = "produits"  # nom de la collection MongoDB
