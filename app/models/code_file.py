from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.utils.database import Base

class CodeFile(Base):
    __tablename__ = "code_files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(120), index=True)
    content = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))