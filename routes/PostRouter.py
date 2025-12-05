from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.PostSchema import CreatePostRequest, UpdatePostRequest
from controllers.PostController import PostController
from db.database import get_db

router = APIRouter(prefix="/api/posts", tags=["post"])


@router.post("", status_code=201)
async def createPost(request: CreatePostRequest, db: Session = Depends(get_db)):
    return PostController.createPost(request, db)


@router.get("")
async def getPosts(db: Session = Depends(get_db)):
    return PostController.getPosts(db)


@router.get("/{post_id}")
async def getPost(post_id: int, db: Session = Depends(get_db)):
    return PostController.getPost(post_id, db)


@router.put("/{post_id}")
async def updatePost(post_id: int, request: UpdatePostRequest, db: Session = Depends(get_db)):
    return PostController.updatePost(post_id, request, db)


@router.delete("/{post_id}")
async def deletePost(post_id: int, email: str, db: Session = Depends(get_db)):
    return PostController.deletePost(post_id, email, db)
