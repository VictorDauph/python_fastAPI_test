from fastapi import APIRouter, Depends
from typing import List

from beanie_models.user_model import User
from controllers.produit_controllers import create_produit, delete_produit, get_produits, get_produit, update_produit
from middlewares.get_current_user import get_current_user
from schemas_validators.prduit_schema import ProduitCreate, ProduitResponse, ProduitUpdate

router = APIRouter(
    prefix="/produits",
    tags=["produits"]
)


@router.get("/",response_model=List[ProduitResponse])
async def get_produits_route(user: User=Depends(get_current_user)) -> List[ProduitResponse]:
    return await get_produits()


@router.get("/{produit_id}",response_model=ProduitResponse)
async def get_produit_route(produit_id: str,user: User=Depends(get_current_user)) -> ProduitResponse:
    return await get_produit(produit_id)

@router.post("/",response_model=ProduitResponse)
async def create_produit_route(produit: ProduitCreate,user: User=Depends(get_current_user)):
    return await create_produit(produit)

@router.delete("/{produit_id}",response_model=dict)
async def delete_produit_route(produit_id: str,user: User=Depends(get_current_user)):
    return await delete_produit(produit_id)

@router.put("/{produit_id}",response_model=ProduitResponse)
async def update_produit_route(produit_id: str, data: ProduitUpdate,user: User=Depends(get_current_user)):
    return await update_produit(produit_id, data)