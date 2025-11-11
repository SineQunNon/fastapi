from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/post", tags=["post"])

class CreatePostRequest(BaseModel):
    title: str
    content: str
    postImage: str | None = None

@router.post("")
async def createPost(request: CreatePostRequest):
    # TODO
    return {"message": "게시글을 성공적으로 작성했습니다."}

@router.get("")
async def getPosts():
    return {"message": "게시글 목록 조회를 완료했습니다."}

