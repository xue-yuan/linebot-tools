from fastapi import APIRouter
from fastapi.responses import JSONResponse


userRouter = APIRouter(
    prefix="/user",
    tags=["user"],
)


@userRouter.post("/login")
async def loging():
    return JSONResponse({"foo", "bar"})


@userRouter.post("/logout")
async def logout():
    return JSONResponse({"foo", "bar"})
