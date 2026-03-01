from sqlalchemy.orm import Session
from models.department import Department

class DepartmentRepository:

    def create(self, db: Session, name: str, description: str):
        dept = Department(name=name, description=description)
        db.add(dept)
        db.commit()
        db.refresh(dept)
        return dept

    def get_by_id(self, db: Session, dept_id: int):
        return db.query(Department).filter(Department.id == dept_id).first()

    def get_by_name(self, db: Session, name: str):
        return db.query(Department).filter(Department.name == name).first()