from fastapi import APIRouter
from typing import List

from controllers.produit_controllers import create_produit, delete_produit, get_produits
from schemas_validators.prduit_schema import ProduitCreate, ProduitResponse

router = APIRouter(
    prefix="/produits",
    tags=["produits"]
)


@router.get("/",response_model=List[ProduitResponse])
async def get_produits_route() -> List[ProduitResponse]:
    return await get_produits()

'''
@router.get("/{produit_id}",response_model=ProduitResponse)
def get_produit_route(produit_id: int) -> ProduitResponse:
    return get_produit(produit_id)
'''
@router.post("/",response_model=ProduitResponse)
async def create_produit_route(produit: ProduitCreate):
    return await create_produit(produit)

@router.delete("/{produit_id}",response_model=dict)
async def delete_produit_route(produit_id: str):
    return await delete_produit(produit_id)
