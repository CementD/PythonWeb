from sqlalchemy.orm import Session

from models.department import Department
from repositories.DepartmentRepository import DepartmentRepository
from repositories.EventRepository import EventRepository
from schemas.department import DepartmentCreate


class DepartmentService:
    def __init__(self, dep_rep: DepartmentRepository, event_rep: EventRepository):
        self.dep_rep = dep_rep
        self.event_rep = event_rep

    def create_department(self, db: Session, dept: DepartmentCreate) -> Department:
        department = self.dep_rep.get_by_name(db, dept.name)
        if department:
            raise ValueError(f"Department {dept.name} already exists")
        return self.dep_rep.create(db, name=dept.name, description=dept.description)

    def add_event_to_department(self, db: Session, department_id: int, event_id: int) -> Department:
