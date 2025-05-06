from typing import List

from fastapi import HTTPException

from schemas_validators.prduit_schema import ProduitResponse, ProduitCreate

fake_db: List[ProduitResponse] = [
    ProduitResponse(produit_id=1, nom="Ordinateur", prix=999),
    ProduitResponse(produit_id=2, nom="Clavier", prix=49),
    ProduitResponse(produit_id=3, nom="Souris", prix=29)
]


def get_produit(produit_id: int) -> ProduitResponse:
    for produit in fake_db:
        if produit.produit_id == produit_id:
            return produit
    raise HTTPException(status_code=404, detail= "Produit non trouvé!")

def get_produits()-> List[ProduitResponse]:
    return fake_db

def create_produit(produit: ProduitCreate)->ProduitResponse:
    new_produit_dict = produit.model_dump()
    new_produit_dict["produit_id"] = len(fake_db) + 1
    new_produit =ProduitResponse(**new_produit_dict)
    fake_db.append(new_produit)
    return new_produit

def delete_produit(produit_id: int):
    global fake_db
    fake_db = [p for p in fake_db if p.produit_id != produit_id]
    return {"message": f"Produit {produit_id} supprimé"}