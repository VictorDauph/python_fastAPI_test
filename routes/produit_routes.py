from fastapi import APIRouter
from typing import List

from controllers.produit_controllers import get_produit, get_produits, create_produit, delete_produit
from schemas_validators.prduit_schema import ProduitCreate, ProduitResponse

router = APIRouter(
    prefix="/produits",
    tags=["produits"]
)


@router.get("/",response_model=List[ProduitResponse])
def get_produits_route() -> List[ProduitResponse]:
    return get_produits()

@router.get("/{produit_id}",response_model=ProduitResponse)
def get_produit_route(produit_id: int) -> ProduitResponse:
    return get_produit(produit_id)

@router.post("/",response_model=ProduitResponse)
def create_produit_route(produit: ProduitCreate):
    return create_produit(produit)

@router.delete("/{produit_id}",response_model=dict)
def delete_produit_route(produit_id: int):
    return delete_produit(produit_id)
