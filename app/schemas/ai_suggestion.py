from pydantic import BaseModel

class AISuggestionCreate(BaseModel):
    code_file_id: int
    suggestion: str

class AISuggestionResponse(BaseModel):
    id: int
    code_file_id: int
    suggestion: str
    status: str

    class Config:
        from_attributes = True