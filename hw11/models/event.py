from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.session import Base
from models.association import user_events

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    date = Column(DateTime)

    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department", back_populates="events")

    users = relationship(
        "User",
        secondary=user_events,
        back_populates="events"
    )