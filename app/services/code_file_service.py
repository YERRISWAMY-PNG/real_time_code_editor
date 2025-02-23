from app.models.code_file import CodeFile
from app.schemas.code_file import CodeFileCreate, CodeFileResponse
from app.utils.database import SessionLocal

class CodeFileService:
    def __init__(self):
        self.db = SessionLocal()

    def create_code_file(self, code_file: CodeFileCreate):
        db_code_file = CodeFile(**code_file.dict())
        self.db.add(db_code_file)
        self.db.commit()
        self.db.refresh(db_code_file)
        return db_code_file