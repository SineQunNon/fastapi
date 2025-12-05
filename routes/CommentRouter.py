from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.CommentSchema import CreateCommentRequest, UpdateCommentRequest
from controllers.CommentController import CommentController
from db.database import get_db

router = APIRouter(prefix="/api", tags=["comment"])

@router.post("/posts/{post_id}/comments", status_code=201)
async def createComment(post_id: int, request: CreateCommentRequest, db: Session = Depends(get_db)):
    return CommentController.createComment(post_id, request, db)


@router.get("/posts/{post_id}/comments")
async def getComments(post_id: int, db: Session = Depends(get_db)):
    return CommentController.getComments(post_id, db)


@router.put("/comments/{comment_id}")
async def updateComment(comment_id: int, request: UpdateCommentRequest, db: Session = Depends(get_db)):
    return CommentController.updateComment(comment_id, request, db)


@router.delete("/comments/{comment_id}")
async def deleteComment(comment_id: int, email: str, db: Session = Depends(get_db)):
    return CommentController.deleteComment(comment_id, email, db)
