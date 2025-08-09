
from beanie import Document
from pydantic import Field
from datetime import datetime

import uuid


class User(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    email: str

    class Settings:
        name = "users"