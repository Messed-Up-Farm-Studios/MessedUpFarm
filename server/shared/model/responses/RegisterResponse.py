from uuid import UUID

from pydantic import BaseModel


class RegisterResponse(BaseModel):
    username: str
    authToken: UUID
