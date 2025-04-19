from fastapi import HTTPException

from app.db.database import post_collection
from datetime import datetime, timezone
from app.models import post_helper
from bson import ObjectId
from pymongo import ReturnDocument

from app.utils import serialize_document


async def create_post(post:dict)->dict:
    now = datetime.now(timezone.utc)
    post["createdAt"] = now
    post["updatedAt"] = now
    res = await post_collection.insert_one(post)
    return post_helper(await post_collection.find_one({"_id": res.inserted_id}))



async def get_all(term: str = None) -> list:
    query = {}
    if term:
        query = {
            "$or": [
                {"title": {"$regex": term, "$options": "i"}},
                {"content": {"$regex": term, "$options": "i"}},
                {"category": {"$regex": term, "$options": "i"}},
            ]
        }
    posts = []
    async for post in post_collection.find(query):
        posts.append(post_helper(post))
    return posts



async def get_post(id: str) -> dict:
    post = await post_collection.find_one({"_id": ObjectId(id)})
    return post_helper(post) if post else None


async def update_post(id: str, data: dict) -> dict:
    data["updatedAt"] = datetime.now(timezone.utc)
    post = await post_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": data},
        return_document=ReturnDocument.AFTER
    )
    return post_helper(post) if post else None

async def delete_post(id: str) -> bool:
    result = await post_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count == 1