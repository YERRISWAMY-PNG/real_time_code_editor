from app.models.ai_suggestion import AISuggestion
from app.schemas.ai_suggestion import AISuggestionCreate, AISuggestionResponse
from app.utils.database import SessionLocal

class AIService:
    def __init__(self):
        self.db = SessionLocal()

    def create_ai_suggestion(self, suggestion: AISuggestionCreate):
        db_suggestion = AISuggestion(**suggestion.dict())
        self.db.add(db_suggestion)
        self.db.commit()
        self.db.refresh(db_suggestion)
        return db_suggestion