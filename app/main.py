from fastapi import FastAPI
from app.api.router import api_router
from contextlib import asynccontextmanager
from app.db.database import init_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True, 
    allow_methods=["*"],  
    allow_headers=["*"], 
)



app.include_router(api_router)

@app.get('/')
async def say_hallo():
    return {'hi'}

