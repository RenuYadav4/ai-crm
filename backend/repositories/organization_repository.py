from sqlalchemy.orm import Session

from models.organization import Organization

class OrganizationRepository: 

    def __init__(self, db: Session):
        print(db)
        self.db=db
    
    def get_by_email(self, email: str):
        return (
            self.db.query(Organization)
            .filter(Organization.email == email)
            .first()
        )
    
    def create(self, organization: Organization):
        try:
            self.db.add(organization)
            self.db.commit()
            self.db.refresh(organization)
            return organization
        except Exception as e:
            self.db.rollback()
            raise e
        
    def get_all(self):
        return self.db.query(Organization).all()
    
    def get_by_id(self, organization_id: int):
        return (
            self.db.query(Organization)
            .filter(Organization.id == organization_id)
            .first()
        )
    
    def update(self):
        self.db.commit()

    def delete(self, organization: Organization):
        self.db.delete(organization)
        self.db.commit()

