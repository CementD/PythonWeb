from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.event import EventCreate, EventRead
from services.EventService import EventService

router = APIRouter(prefix="/events", tags=["Events"])
service = EventService()

@router.post("/", response_model=EventRead)
def create_event(event: EventCreate, creator_role: str = Query(...), db: Session = Depends(get_db)):
    """
    creator_role: роль пользователя, который создает событие (Commander, Scientist, Crew)
    """
    try:
        return service.create_event(db, event, creator_role)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{event_id}/assign/{user_id}")
def assign_user_to_event(event_id: int, user_id: int, db: Session = Depends(get_db)):
    try:
        service.assign_user_to_event(db, user_id, event_id)
        return {"message": "User assigned to event"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/{user_id}", response_model=list[EventRead])
def get_events_for_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_sorted_events_for_user(db, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))