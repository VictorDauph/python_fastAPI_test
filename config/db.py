from beanie import init_beanie
import logging
from motor.motor_asyncio import AsyncIOMotorClient

import os
from dotenv import load_dotenv

from beanie_models.product_model import Produit
from beanie_models.user_model import User

load_dotenv()
logger = logging.getLogger("uvicorn")

async def init_db():
    try:
        mongo_uri = os.getenv("MONGO_URI")
        client = AsyncIOMotorClient(mongo_uri)
        await init_beanie(database=client.get_default_database(), document_models=[Produit,User])
        logger.info("✅ Connexion à MongoDB établie avec succès.")
    except Exception as e:
        logger.error(f"❌ Échec de la connexion à MongoDB : {e}")
        raise