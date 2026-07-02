from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.security import hash_password , verify_password, create_refresh_token, create_access_token
from models.user import User
from repositories.auth_repository import AuthRepository
from schemas.auth import RegisterRequest

class AuthService:

    def __init__(self, db:Session):
        self.repository = AuthRepository(db)
    
    def register(self,  request: RegisterRequest,):
        print("\n========== SERVICE ==========")
        print("[Service] register() called")
        print("[Service] Checking if user already exists")
        existing_user = self.repository.get_user_by_email(request.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered.",
            )
        
        print("[Service] User not found")
        print("[Service] Creating new user")

        hashed_password = hash_password(request.password)

        user = User(
            full_name=request.full_name,
            email=request.email,
            hashed_password=hashed_password,
            organization_id=request.organization_id,
            role_id=request.role_id,
        )

        print("[Service] Saving new user to the database")
        return self.repository.create_user(user)
    

    def login(self, email: str, password: str):
        print("\n========== SERVICE ==========")
        print("[Service] login() called")
        user = self.repository.get_user_by_email(email)

        if not user:
           raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid credentials"
        )

        print("[Service] User found, verifying password")
        if not verify_password(password, user.hashed_password):
           raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid credentials"
            )


        print("[Service] Password verified, generating tokens")
        access_token = create_access_token({
           "user_id": user.id,
           "email": user.email,
           "role_id": user.role_id
        })

        refresh_token, _ = create_refresh_token({
           "user_id": user.id
        })

        return {
           "access_token": access_token,
           "refresh_token": refresh_token,
            "token_type": "bearer",
           "user": user
        }