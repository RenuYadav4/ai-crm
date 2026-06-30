from pydantic import BaseModel, EmailStr, Field, ConfigDict

class RegisterRequest(BaseModel):
    full_name: str = Field(..., min_lenght=3, max_length=255)
    email: EmailStr
    password: str = Field(..., min_length=6)
    organization_id: int
    role_id: int

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    organization_id: int
    role_id: int

    model_config = ConfigDict(from_attributes=True)