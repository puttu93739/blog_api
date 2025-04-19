from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    category: str
    tags: List[str]

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class PostResponse(PostBase):
    id: str
    createdAt: datetime
    updatedAt: datetime
