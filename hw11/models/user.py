from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = relationship("Role", back_populates="users")
    role_id = Column(Integer, ForeignKey("roles.id"))
    events = relationship("Event", secondary="user_events", back_populates="users")
