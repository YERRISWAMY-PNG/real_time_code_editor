from fastapi import APIRouter, Depends
from app.services.ai_service import AIService
from app.schemas.ai_suggestion import AISuggestionCreate, AISuggestionResponse

router = APIRouter()

@router.post("/ai-suggestions/", response_model=AISuggestionResponse)
def create_ai_suggestion(suggestion: AISuggestionCreate, service: AIService = Depends()):
    return service.create_ai_suggestion(suggestion)