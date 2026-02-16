from sqlalchemy.orm import Session
from models.department import Department
from models.event import Event


class DepartmentRepository():
    def create(self, db: Session, name: str, description: str) -> Department:
        department = Department(name=name, description=description)
        db.add(department)
        db.commit()
        db.refresh(department)
        return department

    def get_all(self, db: Session) -> list[Department]:
        return db.query(Department).all()

    def get_by_id(self, db: Session, id: int) -> Department | None:
        return db.query(Department).filter(Department.id == id).first()

    def get_by_name(self, db: Session, name: str) -> Department | None:
        return db.query(Department).filter(Department.name == name).first()

    def add_event(self, department: Department, event: Event) -> None:
        department.events.append(event)