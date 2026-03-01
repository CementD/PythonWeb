from sqlalchemy.orm import Session
from models.event import Event

class EventRepository:

    def create(self, db: Session, title: str, description: str, date, department_id: int):
        event = Event(
            title=title,
            description=description,
            date=date,
            department_id=department_id
        )
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    def get_by_id(self, db: Session, event_id: int):
        return db.query(Event).filter(Event.id == event_id).first()

    def get_all(self, db: Session):
        return db.query(Event).all()