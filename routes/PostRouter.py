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
    return {"message": "게시글을 성공적으로 성공했습니다."}

@router.get("")
async def getPosts():
    return {"message": "게시글 목록 조회를 성공했습니다."}

@router.get("/{post_id}")
async def getPost(post_id: int):
    return {"message" : "게시글 상세 조회를 성공했습니다."}
