from sqlalchemy.orm import Session
from models.role import Role

class RoleRepository:

    def create(self, db: Session, name: str):
        role = Role(name=name)
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def get_by_name(self, db: Session, name: str):
        return db.query(Role).filter(Role.name == name).first()