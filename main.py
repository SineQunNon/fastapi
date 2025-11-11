from routes import LoginRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(LoginRouter.router)
