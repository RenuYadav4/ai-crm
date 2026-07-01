from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from services.auth.auth_service import AuthService
import traceback


from schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
    UserResponse
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


# -------------------------
# REGISTER
# -------------------------
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
        service = AuthService(db)
        return service.register(request)
   


# -------------------------
# LOGIN
# -------------------------
@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK
)
def login(request: LoginRequest, db: Session = Depends(get_db)):
        service = AuthService(db)

        result = service.login(
            email=request.email,
            password=request.password
        )

        return result
