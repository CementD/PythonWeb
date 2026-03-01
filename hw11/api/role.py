from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.role import RoleCreate, RoleRead
from services.RoleService import RoleService

router = APIRouter(prefix="/roles", tags=["Roles"])
service = RoleService()

@router.post("/", response_model=RoleRead)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    try:
        return service.create_role(db, role)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))