from datetime import datetime
from sqlalchemy.orm import Session

from models.department import Department
from models.event import Event
from models.user import User


class EventRepository():
    def create(self, db: Session, name: str, description: str, date: datetime) -> Event:
        event = Event(name=name, description=description, date=date)
        db.add(event)
        return event

    def get_all(self, db: Session) -> list[type[Event]]:
        return db.query(Event).all()

    def get_by_id(self, db: Session, id: int) -> Event | None:
        return db.query(Event).filter(Event.id == id).first()

    def get_by_name(self, db: Session, name: str) -> Event | None:
        return db.query(Event).filter(Event.name == name).first()

    def get_by_date(self, db: Session, date: datetime) -> Event | None:
        return db.query(Event).filter(Event.date == date).first()

    def add_user(self, user: User, event: Event) -> None:
        event.users.append(user)

    def get_by_user(self, db: Session, user_id: int) -> list[Event] | None:
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            return []
        return user.events

    def get_by_department(self, db: Session, department_id: int) -> list[Event] | None:
        department = db.query(Department).filter(Department.id == department_id).first()
        if department is None:
            return []
        return department.events