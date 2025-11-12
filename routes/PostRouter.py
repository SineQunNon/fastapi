from fastapi import APIRouter
from controller.PostController import CreatePostRequest, PostController, UpdatePostRequest

router = APIRouter(prefix="/post", tags=["post"])

@router.post("")
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
async def deletePost(post_id: int):
    return PostController.deletePost(post_id)
