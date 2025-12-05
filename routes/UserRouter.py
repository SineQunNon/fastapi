from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.UserController import UserController
from schemas.UserSchema import RegisterRequest, UpdateUserRequest, UpdateNicknameRequest, UpdatePasswordRequest
from db.database import get_db

router = APIRouter(prefix="/api/users", tags=["user"])

@router.post("/register")
async def register(request: RegisterRequest, db: Session = Depends(get_db)):
    return UserController.register(request, db)

@router.get("/")
async def getUsers(db: Session = Depends(get_db)):
    return UserController.getUsers(db)

@router.get("/{email}")
async def getUser(email: str, db: Session = Depends(get_db)):
    return UserController.getUser(email, db)

@router.patch("/nickname")
async def updateNickname(request: UpdateNicknameRequest, db: Session = Depends(get_db)):
    return UserController.updateNickname(request, db)

@router.patch("/password")
async def updatePassword(request: UpdatePasswordRequest, db: Session = Depends(get_db)):
    return UserController.updatePassword(request, db)

@router.put("/{email}")
async def updateNicknameAndImage(email: str, request: UpdateUserRequest, db: Session = Depends(get_db)):
    return UserController.updateUser(email, request, db)

@router.delete("/{email}")
async def deleteUser(email: str, db: Session = Depends(get_db)):
    return UserController.deleteUser(email, db)
