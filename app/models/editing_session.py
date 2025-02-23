from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.utils.database import Base

class EditingSession(Base):
    __tablename__ = "editing_sessions"
    id = Column(Integer, primary_key=True, index=True)
    code_file_id = Column(Integer, ForeignKey("code_files.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)