from fastapi import APIRouter

from api.v1.keyword import keywordRouter
from api.v1.user import userRouter

v1Router = APIRouter(
    prefix="/v1",
    tags=["v1"],
)

v1Router.include_router(keywordRouter)
v1Router.include_router(userRouter)
