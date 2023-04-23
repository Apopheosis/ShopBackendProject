from pydantic import BaseModel, EmailStr, Field, validator, UUID4
from datetime import datetime
from typing import Optional
class UserCreate(BaseModel):
    email: EmailStr
    name: str
    password: str
    name: str

class UserBase(BaseModel):
    id: int
    email: EmailStr
    name: str

class TokenBase(BaseModel):
    token: UUID4 = Field(..., alias="access_token")
    expires: datetime
    token_type: Optional[str] = "bearer"

    class Config:
        allow_population_by_field_name = True

    @validator("token")
    def hexlify_token(cls, value):
        return value.hex

class User(UserBase):
    token: TokenBase = {}