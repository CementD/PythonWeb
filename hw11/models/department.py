from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    events = relationship("Event", back_populates="department")