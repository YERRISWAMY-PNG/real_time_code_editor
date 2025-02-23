from pydantic import BaseModel

class CodeFileCreate(BaseModel):
    filename: str
    content: str
    owner_id: int

class CodeFileResponse(BaseModel):
    id: int
    filename: str
    content: str
    owner_id: int

    class Config:
        from_attributes = True