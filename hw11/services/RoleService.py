from sqlalchemy.orm import Session
from repositories.RoleRepository import RoleRepository
from schemas.role import RoleCreate

class RoleService:

    def __init__(self):
        self.repo = RoleRepository()

    def create_role(self, db: Session, role: RoleCreate):
        existing = self.repo.get_by_name(db, role.name)
        if existing:
            raise ValueError(f"Role {role.name} already exists")
        return self.repo.create(db, role.name)

    def get_role_by_name(self, db: Session, name: str):
        return self.repo.get_by_name(db, name)