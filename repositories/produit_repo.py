from beanie import PydanticObjectId
from typing import List, Optional
from beanie_models.product_model import Produit
from schemas_validators.prduit_schema import ProduitCreate, ProduitResponse, ProduitUpdate


async def create_produit_repo(data: ProduitCreate) -> Produit:
    produit_to_create = Produit(**data.model_dump())
    return await produit_to_create.insert()

async def get_produit_repo(produit_id: PydanticObjectId) -> Optional[Produit]:
    return await Produit.get(produit_id)

async def get_produits_repo() -> List[Produit]:
    return await Produit.find_all().to_list()

async def update_produit_repo(produit_id: PydanticObjectId, data: ProduitUpdate) -> Optional[Produit]:
    produit = await Produit.get(produit_id)
    if produit:
        if data.nom is not None:
            produit.nom = data.nom
        if data.prix is not None:
            produit.prix = data.prix
        await produit.save()
        return produit
    return None

async def delete_produit_repo(produit_id: PydanticObjectId) -> bool:
    produit = await Produit.get(produit_id)
    if produit:
        await produit.delete()
        return True
    return False

