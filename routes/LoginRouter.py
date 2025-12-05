from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.LoginController import LoginController
from schemas.UserSchema import LoginRequest
from db.database import get_db

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    return LoginController.login(request, db)
