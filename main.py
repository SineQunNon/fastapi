from routes import CommentRouter, LoginRouter, UserRouter, PostRouter, SummarizationRouter
from fastapi import FastAPI

app = FastAPI()

app.include_router(LoginRouter.router)
app.include_router(UserRouter.router)
app.include_router(PostRouter.router)
app.include_router(CommentRouter.router)
app.include_router(SummarizationRouter.router)
