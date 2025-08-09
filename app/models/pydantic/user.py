
from pydantic import BaseModel
from uuid import UUID


class GetUserProfil(BaseModel):
    id: UUID

class SetNewUser(BaseModel):
    username: str
    email: str