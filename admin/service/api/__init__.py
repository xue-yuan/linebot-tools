from fastapi import APIRouter
from fastapi.responses import JSONResponse

from api.v1 import v1Router


apiRouter = APIRouter(
    prefix="/api",
    tags=["api"],
)

apiRouter.include_router(v1Router)


@apiRouter.get("/heartbeat")
def heartbeat():
    return JSONResponse({"foo", "bar"})
