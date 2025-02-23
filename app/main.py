from fastapi import FastAPI
from app.api import users, code_files, ai
from app.utils.database import engine, Base

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(code_files.router)
app.include_router(ai.router)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Real-Time Collaborative Code Editor!"}