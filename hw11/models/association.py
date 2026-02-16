from sqlalchemy import Column, Integer, ForeignKey, Table
from db.session import Base

user_events = Table(
    'user_events',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('event_id', Integer, ForeignKey('event.id'))
)