from sqlalchemy.orm import Session
from repositories.UserRepository import UserRepository
from repositories.RoleRepository import RoleRepository
from schemas.user import UserCreate

class UserService:

    def __init__(self):
        self.repo = UserRepository()
        self.role_repo = RoleRepository()

    def create_user(self, db: Session, user: UserCreate):
        role = self.role_repo.get_by_name(db, user.role_id)
        if not role:
            raise ValueError(f"Role with id {user.role_id} does not exist")
        return self.repo.create(db, user.name, user.role_id)

    def get_user_by_id(self, db: Session, user_id: int):
        return self.repo.get_by_id(db, user_id)

    def get_all_users(self, db: Session):
        return self.repo.get_all(db)