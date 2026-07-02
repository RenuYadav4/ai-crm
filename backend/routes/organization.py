from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)
from services.companies.organization_service import OrganizationService
router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_organization(
    request: OrganizationCreate,
    db: Session = Depends(get_db),
):
    return OrganizationService(db).create(request)


@router.get(
    "",
    response_model=list[OrganizationResponse],
)
def get_all(db: Session = Depends(get_db)):
    return OrganizationService(db).get_all()


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_by_id(
    organization_id: int,
    db: Session = Depends(get_db),
):
    return OrganizationService(db).get_by_id(organization_id)


@router.put(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def update(
    organization_id: int,
    request: OrganizationUpdate,
    db: Session = Depends(get_db),
):
    return OrganizationService(db).update(
        organization_id,
        request,
    )


@router.delete(
    "/{organization_id}",
)
def delete(
    organization_id: int,
    db: Session = Depends(get_db),
):
    return OrganizationService(db).delete(organization_id)