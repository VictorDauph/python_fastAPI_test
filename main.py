
import sys
from contextlib import asynccontextmanager

from config.db import init_db
from routes import produit_routes

print("Python utilisé :", sys.executable)


from fastapi import FastAPI

@asynccontextmanager
async def lifespan(_app: FastAPI):
    await init_db()
    yield  # ici tu pourrais ajouter des actions de shutdown plus tard

# ✅ App avec gestion du cycle de vie
app = FastAPI(lifespan=lifespan)


#import route de test
@app.get("/")
def lire_racine():
    return {"message": "Bienvenue, petite flamme !!!!"}

#import sous-router
app.include_router(produit_routes.router)