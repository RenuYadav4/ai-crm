from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.security import hash_password
from models.user import User
from repositories.auth_repository import AuthRepository
from schemas.auth import RegisterRequest

class AuthService:

    def __init__(self, db:Session):
        self.repository = AuthRepository(db)
    
    def register(self,  request: RegisterRequest,):
        existing_user = self.repository.get_user_by_email(request.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered.",
            )
        
        hashed_password = hash_password(request.password)

        user = User(
            full_name=request.full_name,
            email=request.email,
            hashed_password=hashed_password,
            organization_id=request.organization_id,
            role_id=request.role_id,
        )

        return self.repository.create_user(user)