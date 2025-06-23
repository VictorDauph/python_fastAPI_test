from typing import List

from beanie import PydanticObjectId
from fastapi import HTTPException

from beanie_models.product_model import Produit
from repositories.produit_repo import create_produit_repo, delete_produit_repo, get_produits_repo, get_produit_repo, \
    update_produit_repo
from schemas_validators.prduit_schema import ProduitResponse, ProduitCreate, ProduitUpdate

'''
fake_db: List[ProduitResponse] = [
    ProduitResponse(produit_id=1, nom="Ordinateur", prix=999),
    ProduitResponse(produit_id=2, nom="Clavier", prix=49),
    ProduitResponse(produit_id=3, nom="Souris", prix=29)
]
'''


async def get_produit(produit_id: str) -> ProduitResponse:
    produit = await get_produit_repo(PydanticObjectId(produit_id))
    if produit:
        return ProduitResponse(**produit.model_dump(include={"id", "nom", "prix"}))
    raise HTTPException(status_code=404, detail= "Produit non trouvé!")

async def get_produits()-> List[ProduitResponse]:
    list_produits = await get_produits_repo()

    list_produits_response:List[ProduitResponse]=[ ProduitResponse(**produit.model_dump(include={"id", "nom", "prix"})) for produit in list_produits]
    return list_produits_response

async  def create_produit(produit: ProduitCreate)->ProduitResponse:

    #new_produit_dict = produit.model_dump()
    #new_produit_dict["produit_id"] = len(fake_db) + 1
    #new_produit =ProduitResponse(**new_produit_dict)
    new_produit: Produit =await create_produit_repo(produit)
    return ProduitResponse(**new_produit.model_dump(include={"id", "nom", "prix"}))

async def delete_produit(produit_id: str):
    produit_object_id = PydanticObjectId(produit_id)
    res = await delete_produit_repo(produit_object_id)
    if res:
        return {"message": f"Produit {produit_object_id} supprimé"}
    return {"message": "échec suppression"}

async def update_produit(produit_id: str, data: ProduitUpdate):
    produit_object_id = PydanticObjectId(produit_id)
    new_produit = await update_produit_repo(produit_object_id, data)
    if new_produit:
        return ProduitResponse(**new_produit.model_dump(include={"id", "nom", "prix"}))
    raise HTTPException(status_code=404, detail= "Produit non trouvé!")