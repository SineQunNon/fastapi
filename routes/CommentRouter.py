from fastapi import APIRouter, Header
from typing import Optional
from schemas.CommentSchema import CreateCommentRequest, UpdateCommentRequest
from controllers.CommentController import CommentController

router = APIRouter(prefix="/api", tags=["comment"])

@router.post("/posts/{post_id}/comments", status_code=201)
async def createComment(post_id: int, request: CreateCommentRequest):
    return CommentController.createComment(post_id, request)


@router.get("/posts/{post_id}/comments")
async def getComments(post_id: int):
    return CommentController.getComments(post_id)


@router.put("/comments/{comment_id}")
async def updateComment(comment_id: int, request: UpdateCommentRequest):
    return CommentController.updateComment(comment_id, request)


@router.delete("/comments/{comment_id}")
async def deleteComment(comment_id: int, email: str):
    return CommentController.deleteComment(comment_id, email)
