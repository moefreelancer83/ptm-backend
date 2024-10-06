from fastapi import FastAPI
from app.api.router import api_router
from contextlib import asynccontextmanager
from app.db.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(api_router)

@app.get('/')
async def say_hallo():
    return {'hi'}

