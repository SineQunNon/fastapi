from fastapi import APIRouter
from controller.UserController import RegisterRequest, UserController, UpdateUserRequest

router = APIRouter(prefix="/users", tags=["user"])

@router.post("/register")
async def register(request: RegisterRequest):
    return UserController.register(request)

@router.put("/{email}")
async def updateUser(email: str, request: UpdateUserRequest):
    return UserController.updateUser(email, request)

@router.delete("/{email}")
async def deleteUser(email: str):
    return UserController.deleteUser(email)

