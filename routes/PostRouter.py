from fastapi import APIRouter
from schemas.PostSchema import CreatePostRequest, UpdatePostRequest
from controllers.PostController import PostController

router = APIRouter(prefix="/api/posts", tags=["post"])


@router.post("", status_code=201)
async def createPost(request: CreatePostRequest):
    return PostController.createPost(request)


@router.get("")
async def getPosts():
    return PostController.getPosts()


@router.get("/{post_id}")
async def getPost(post_id: int):
    return PostController.getPost(post_id)


@router.put("/{post_id}")
async def updatePost(post_id: int, request: UpdatePostRequest):
    return PostController.updatePost(post_id, request)


@router.delete("/{post_id}")
async def deletePost(post_id: int, email: str):
    return PostController.deletePost(post_id, email)
