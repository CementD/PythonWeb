from typing import List

from sqlalchemy.orm import Session

from models.role import Role
from models.user import User


class RoleRepository:
    def create(self, db: Session, name: str) -> Role:
        role = Role(name=name)
        db.add(role)
        return role

    def get_all(self, db: Session) -> list[Role]:
        return db.query(Role).all()

    def get_by_id(self, db: Session, id: int) -> Role | None:
        return db.query(Role).filter(Role.id == id).first()

    def get_by_name(self, db: Session, name: str) -> Role | None:
        return db.query(Role).filter(Role.name == name).first()

    def get_by_user(self, db: Session, user_id: int) -> Role | None:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return None
        return user.role