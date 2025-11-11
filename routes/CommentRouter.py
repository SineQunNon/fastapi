from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/comment", tags=["comment"])

class CreateCommentRequest(BaseModel):
    post_id: int
    content: str

@router.post("")
async def createComment(request: CreateCommentRequest):
    return {"message" : "댓글 작성을 성공적으로 완료했습니다."}

@router.get("/{post_id}")
async def getComments(post_id: int):
    return {"message" : "댓글 조회를 성공적으로 마쳤습니다"}

class UpdateCommentRequest(BaseModel):
    content: str

@router.put("/{comment_id}")
async def updateComment(comment_id: int, request:UpdateCommentRequest):
    return {"message" : "댓글 수정을 성공적으로 완료했습니다"}

@router.delete("/{comment_id}")
async def deleteComment(comment_id: int):
    return {"message" : "댓글을 성공적으로 삭제했습니다"}
