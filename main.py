
import sys

from routes import produit_routes

print("Python utilisé :", sys.executable)


from fastapi import FastAPI

app = FastAPI()

#import route de test
@app.get("/")
def lire_racine():
    return {"message": "Bienvenue, petite flamme !!!!"}

#import sous-router
app.include_router(produit_routes.router)