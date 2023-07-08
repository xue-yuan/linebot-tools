from fastapi import FastAPI

import database
from api import apiRouter
from logger import logger


app = FastAPI()
database.initialize()

app.include_router(apiRouter)
logger.info("[!] Start API Service")
