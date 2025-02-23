from sqlalchemy import Column, Integer, ForeignKey, Text, String
from app.utils.database import Base

class AISuggestion(Base):
    __tablename__ = "ai_suggestions"
    id = Column(Integer, primary_key=True, index=True)
    code_file_id = Column(Integer, ForeignKey("code_files.id"))
    suggestion = Column(Text)
    status = Column(String(20))