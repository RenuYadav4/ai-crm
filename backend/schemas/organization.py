from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr

class OrganizationCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str]= None
    website: Optional[str] = None

class OrganizationUpdate(BaseModel):
    name:Optional[str]=None
    email: Optional[EmailStr]=None
    phone: Optional[str]=None
    website: Optional[str]=None
    logo_url: Optional[str]=None
    description: Optional[str]=None
    industry: Optional[str]=None
    address: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    country: Optional[str]=None
    postal_code: Optional[str]=None
    timezone: Optional[str]=None
    currency: Optional[str]=None
    is_active: Optional[bool]=None

class OrganizationResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str]
    website: Optional[str]
    logo_url: Optional[str]
    description: Optional[str]
    industry: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    timezone: Optional[str]
    currency: Optional[str]
    is_active: bool
    