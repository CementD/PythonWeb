from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(DateTime)
    department = relationship("Department", back_populates="events")
    department_id = Column(Integer, ForeignKey("departments.id"))
    users = relationship("User", secondary="user_events", back_populates="events")