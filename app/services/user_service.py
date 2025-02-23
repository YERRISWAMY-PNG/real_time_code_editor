from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.utils.database import SessionLocal

class UserService:
    def __init__(self):
        self.db = SessionLocal()

    def create_user(self, user: UserCreate):
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user