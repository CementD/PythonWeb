from fastapi import APIRouter
from schemas.feedback import FeedbackResponse, FeedbackCreate

router = APIRouter(
    prefix="/feedback",
    tags=["Feedback"]
)

@router.post("/", response_model=FeedbackResponse)
def create_feedback(feedback: FeedbackCreate):
    return feedback