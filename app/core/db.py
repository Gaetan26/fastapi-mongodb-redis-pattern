
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from beanie import init_beanie

from models.beanie.user import User

import os


load_dotenv()

async def init_db():
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    await init_beanie(
        database=client.your_target_db, 
        document_models=[
            User
        ]
    )