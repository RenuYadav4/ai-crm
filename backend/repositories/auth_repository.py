from datetime import datetime

from sqlalchemy.orm import Session

from models.user import User

from models.refresh_token import RefreshToken

class AuthRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_user_by_email(self,email: str,):
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )
    
    def create_user(self, user:User,):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
    
    def save_refresh_token(self, token: str, expires_at: datetime, user_id: str,):
        refresh = RefreshToken(
            token=token,
            expires_at=expires_at,
            user_id=user_id,
        )

        self.db.add(refresh)
        self.db.commit()
        self.db.refresh(refresh)

        return refresh
    
    def get_refresh_token(self, token:str,):
        return (
            self.db.query(RefreshToken)
            .filter(
                RefreshToken.token == token
            )
            .first()
        )

    def delete_refresh_token(self, token: RefreshToken,):
        self.db.delete(token)

        self.db.commit()   

