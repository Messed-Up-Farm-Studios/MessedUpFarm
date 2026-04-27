from uuid import UUID

from pydantic import BaseModel


class RegisterResult(BaseModel):
    username: str
    authToken: UUID
