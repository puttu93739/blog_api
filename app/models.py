from datetime import datetime
from typing import List
from bson import ObjectId

def post_helper(post) -> dict:
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "content": post["content"],
        "category": post["category"],
        "tags": post["tags"],
        "createdAt": post["createdAt"],
        "updatedAt": post["updatedAt"],
    }

