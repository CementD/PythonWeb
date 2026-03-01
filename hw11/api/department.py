from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.department import DepartmentCreate, DepartmentRead
from services.DepartmentService import DepartmentService

router = APIRouter(prefix="/departments", tags=["Departments"])
service = DepartmentService()

@router.post("/", response_model=DepartmentRead)
def create_department(dept: DepartmentCreate, db: Session = Depends(get_db)):
    try:
        return service.create_department(db, dept)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{dept_id}/events")
def get_department_events(dept_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_department_events(db, dept_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))