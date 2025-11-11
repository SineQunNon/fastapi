from routes import LoginRouter, UserRouter, PostRouter, CommentRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(LoginRouter.router)
app.include_router(UserRouter.router)
app.include_router(PostRouter.router)
app.include_router(CommentRouter.router)
