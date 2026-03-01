from sqlalchemy.orm import Session
from repositories.EventRepository import EventRepository
from repositories.UserRepository import UserRepository
from schemas.event import EventCreate
from models.event import Event

class EventService:

    def __init__(self):
        self.event_repo = EventRepository()
        self.user_repo = UserRepository()

    def create_event(self, db: Session, event: EventCreate, creator_role: str):
        # Проверка ролей
        if creator_role != "Commander":
            raise ValueError("Only Commander can create events")

        return self.event_repo.create(
            db,
            title=event.title,
            description=event.description,
            date=event.date,
            department_id=event.department_id
        )

    def assign_user_to_event(self, db: Session, user_id: int, event_id: int):
        user = self.user_repo.get_by_id(db, user_id)
        event = self.event_repo.get_by_id(db, event_id)

        if not user or not event:
            raise ValueError("User or Event not found")

        for e in user.events:
            if e.date == event.date:
                raise ValueError("User already has an event at this time")

        if len(event.users) >= 5:
            raise ValueError("Event already has 5 participants")

        event.users.append(user)
        db.commit()
        db.refresh(event)

    def get_sorted_events_for_user(self, db: Session, user_id: int):
        user = self.user_repo.get_by_id(db, user_id)
        if not user:
            raise ValueError("User not found")

        events = user.events

        def calc_priority(e: Event):
            n = len(e.users)
            if n > 3:
                return "High"
            if 2 <= n <= 3:
                return "Medium"
            return "Low"

        for e in events:
            e.priority = calc_priority(e)

        return sorted(
            events,
            key=lambda e: (
                {"High": 0, "Medium": 1, "Low": 2}[e.priority],
                e.date
            )
        )