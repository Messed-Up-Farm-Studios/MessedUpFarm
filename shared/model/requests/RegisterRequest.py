from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    username: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Player's Username",
        example="pnobscot",
    )
    age: int = Field(ge=13, le=100, description="Players Age", example=23)
    password: str = Field(description="Players Password", example="admin123")
