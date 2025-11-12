from fastapi import APIRouter
from controller.LoginController import LoginController, LoginRequest

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/")
async def login(request: LoginRequest):
    return LoginController.login(request)
