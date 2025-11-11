from routes import LoginRouter, UserRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(LoginRouter.router)
app.include_router(UserRouter.router)
