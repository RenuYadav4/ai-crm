from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.organization import Organization
from repositories.organization_repository import OrganizationRepository

from schemas.organization import (OrganizationCreate, OrganizationUpdate,)

class OrganizationService:
    def __init__(self, db: Session):
        self.repository = OrganizationRepository(db)

    def create(self, request: OrganizationCreate):
        existing_organization = self.repository.get_by_email(request.email)
        if existing_organization:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Organization with this email already exists.",
            )
        new_organization = Organization(**request.dict())
        return self.repository.create(new_organization)

    def get_by_id(self, organization_id: int):
        return self.repository.get_by_id(organization_id)
    
    def get_all(self):
        return self.repository.get_all()

    def update(self, organization_id: int, request: OrganizationUpdate):
        organization = self.repository.get_by_id(organization_id)
        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found.",
            )
        for key, value in request.dict(exclude_unset=True).items():
            setattr(organization, key, value)
        self.repository.update()
        return organization

    def delete(self, organization_id: int):
        organization = self.repository.get_by_id(organization_id)
        if not organization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found.",
            )
        self.repository.delete(organization)