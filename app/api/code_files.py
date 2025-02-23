from fastapi import APIRouter, Depends
from app.services.code_file_service import CodeFileService
from app.schemas.code_file import CodeFileCreate, CodeFileResponse

router = APIRouter()

@router.post("/code-files/", response_model=CodeFileResponse)
def create_code_file(code_file: CodeFileCreate, service: CodeFileService = Depends()):
    return service.create_code_file(code_file)