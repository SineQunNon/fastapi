from routes import CommentRouter, LoginRouter, UserRouter, PostRouter, SummarizationRouter
from fastapi import FastAPI
from db.database import engine, Base

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(LoginRouter.router)
app.include_router(UserRouter.router)
app.include_router(PostRouter.router)
app.include_router(CommentRouter.router)
app.include_router(SummarizationRouter.router)
