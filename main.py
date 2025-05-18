
import sys
from contextlib import asynccontextmanager
from fastapi import Request
from beanie_models.user_model import User
from config.db import init_db
from middlewares.get_current_user import get_current_user
from routes import produit_routes, auth_routes

print("Python utilisé :", sys.executable)


from fastapi import FastAPI, Depends


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await init_db()
    yield  # ici tu pourrais ajouter des actions de shutdown plus tard

# ✅ App avec gestion du cycle de vie
app = FastAPI(lifespan=lifespan)


#import route de test
@app.get("/")
async def lire_racine(user: User=Depends(get_current_user)):
    return {"message": f"Bienvenue, {user.username} !"}

#import sous-router
app.include_router(produit_routes.router)
app.include_router(auth_routes.router)