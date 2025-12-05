from fastapi import APIRouter
from controllers.UserController import RegisterRequest, UserController, UpdateUserRequest
from schemas.UserSchema import UpdateNicknameRequest, UpdatePasswordRequest

router = APIRouter(prefix="/api/users", tags=["user"])

@router.post("/register")
async def register(request: RegisterRequest):
    return UserController.register(request)

@router.get("/")
async def getUsers():
    return UserController.getUsers()

@router.get("/{email}")
async def getUser(email: str):
    return UserController.getUser(email)

@router.patch("/nickname")
async def updateNickname(request: UpdateNicknameRequest):
    return UserController.updateNickname(request)

@router.patch("/password")
async def updatePassword(request: UpdatePasswordRequest):
    return UserController.updatePassword(request)

@router.put("/{email}")
async def updateNicknameAndImage(email: str, request: UpdateUserRequest):
    return UserController.updateUser(email, request)

@router.delete("/{email}")
async def deleteUser(email: str):
    return UserController.deleteUser(email)

