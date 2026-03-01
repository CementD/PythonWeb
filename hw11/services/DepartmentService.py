from sqlalchemy.orm import Session
from repositories.DepartmentRepository import DepartmentRepository
from repositories.EventRepository import EventRepository
from schemas.department import DepartmentCreate

class DepartmentService:

    def __init__(self):
        self.dep_rep = DepartmentRepository()
        self.event_rep = EventRepository()

    def create_department(self, db: Session, dept: DepartmentCreate):
        department = self.dep_rep.get_by_name(db, dept.name)
        if department:
            raise ValueError(f"Department {dept.name} already exists")

        return self.dep_rep.create(db, dept.name, dept.description)

    def add_event_to_department(self, db: Session, department_id: int, event_id: int):
        department = self.dep_rep.get_by_id(db, department_id)
        event = self.event_rep.get_by_id(db, event_id)

        if not department or not event:
            raise ValueError("Department or Event not found")

        event.department_id = department_id
        db.commit()
        db.refresh(event)
        return department

    def get_department_events(self, db: Session, department_id: int):
        department = self.dep_rep.get_by_id(db, department_id)
        if not department:
            raise ValueError("Department not found")
        return department.events