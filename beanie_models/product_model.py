from beanie import Document
from pydantic import Field
from typing import Optional


class Produit(Document):
    nom: str
    prix: float
    description: Optional[str] = None

    class Settings:
        name = "produits"  # nom de la collection MongoDB
