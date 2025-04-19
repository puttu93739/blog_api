from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes import posts


app = FastAPI()
# Configure CORS
origins = [
    "*",
]
# origins = ["http://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "API is working"}

app.include_router(posts.router, prefix="/posts", tags=["Posts"])
