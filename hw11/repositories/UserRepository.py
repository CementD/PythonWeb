from sqlalchemy.orm import Session
from models.user import User

class UserRepository:
    def create(self, db: Session, name: str, role_id: int) -> User:
        user = User(name=name, role_id=role_id)
        db.add(user)
        return user

    def get_all(self, db: Session) -> list[User]:
        return db.query(User).all()

    def get_by_id(self, db: Session, id: int) -> User | None:
        return db.query(User).filter(User.id == id).first()