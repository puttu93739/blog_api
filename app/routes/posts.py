from fastapi import APIRouter,HTTPException,status

from app.schemas import PostCreate, PostResponse, PostUpdate
from app import crud as crud_post

from typing import List, Optional
router = APIRouter()

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create(post:PostCreate):
    return await crud_post.create_post(post.model_dump())

@router.get("/{id}", response_model=PostResponse)
async def read(id: str):
    post = await crud_post.get_post(id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/", response_model=List[PostResponse])
async def read_all_posts():
    return await crud_post.get_all()

@router.put("/{id}", response_model=PostResponse)
async def update(id: str, post: PostUpdate):
    updated = await crud_post.update_post(id, post.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    deleted = await crud_post.delete_post(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")