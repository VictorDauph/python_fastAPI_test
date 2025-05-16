from beanie import PydanticObjectId
from typing import List, Optional
from beanie_models.product_model import Produit
from schemas_validators.prduit_schema import ProduitCreate, ProduitResponse


async def create_produit_repo(data: ProduitCreate) -> Produit:
    produit_to_create = Produit(**data.model_dump())
    return await produit_to_create.insert()

'''
async def get_produit(produit_id: PydanticObjectId) -> Optional[Produit]:
return await Produit.get(produit_id)
'''

async def get_produits_repo() -> List[Produit]:
    return await Produit.find_all().to_list()

'''
async def update_produit(produit_id: PydanticObjectId, data: ProduitCreate) -> Optional[Produit]:
produit = await Produit.get(produit_id)
if produit:
produit.nom = data.nom
produit.prix = data.prix
await produit.save()
return produit
'''

async def delete_produit_repo(produit_id: PydanticObjectId) -> bool:
    produit = await Produit.get(produit_id)
    if produit:
        await produit.delete()
        return True
    return False

