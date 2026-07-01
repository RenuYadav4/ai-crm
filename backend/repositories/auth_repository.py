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
        try:
           self.db.add(user)
           self.db.commit()
           self.db.refresh(user)

           return user
        except:
            self.db.rollback()
            raise
    
    def save_refresh_token(self, token: str, expires_at: datetime, user_id: str,):
        try:
          refresh = RefreshToken(
             token=token,
             expires_at=expires_at,
             user_id=user_id,
          )

          self.db.add(refresh)
          self.db.commit()
          self.db.refresh(refresh)

          return refresh

        except Exception:
          self.db.rollback()
          raise    
    
    def get_refresh_token(self, token:str,):
        return (
            self.db.query(RefreshToken)
            .filter(
                RefreshToken.token == token
            )
            .first()
        )

    def delete_refresh_token(self, refresh_token: RefreshToken,):
        try:
            self.db.delete(refresh_token)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise
