from fastapi import APIRouter
from fastapi.responses import JSONResponse

from enum import Enum


keywordRouter = APIRouter(
    prefix="/keywords",
    tags=["keyword"],
)


class KeywordType(Enum):
    MENU = 0
    TEXT = 1
    FILE = 2
    IMAGE = 3


@keywordRouter.get("")
async def get_keywords():
    return JSONResponse([{"foo", "bar"}])


@keywordRouter.put("")
async def update_keywords():
    return JSONResponse([{"foo", "bar"}])
