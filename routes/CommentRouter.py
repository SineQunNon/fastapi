from fastapi import APIRouter

from controller.CommentController import CreateCommentRequest, UpdateCommentRequest, CommentController

router = APIRouter(prefix="/comment", tags=["comment"])

@router.post("")
async def createComment(request: CreateCommentRequest):
    return CommentController.createComment(request)

@router.get("/{post_id}")
async def getComments(post_id: int):
    return CommentController.getComments(post_id)

@router.put("/{comment_id}")
async def updateComment(comment_id: int, request:UpdateCommentRequest):
    return CommentController.updateComment(comment_id, request)

@router.delete("/{comment_id}")
async def deleteComment(comment_id: int):
    return CommentController.deleteComment(comment_id)
