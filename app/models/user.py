from sqlalchemy import Column, Integer, String
from app.utils.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, index=True)
    email = Column(String(120), unique=True, index=True)
    password = Column(String(120))
    role = Column(String(20))