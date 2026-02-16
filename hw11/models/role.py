from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.session import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship("User", back_populates="role")