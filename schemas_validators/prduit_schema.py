from pydantic import BaseModel, Field

class ProduitCreate(BaseModel):
    nom: str = Field(..., min_length=2, example="Clavier mécanique")
    prix: float = Field(..., gt=0, example=79.99)

class ProduitResponse(BaseModel):
    produit_id: int
    nom: str
    prix: float
