from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import socketio
from app.logger import get_logger


logger=get_logger(__name__)

sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*', 
    logger=False,
    engineio_logger=False,
    ping_timeout=120,       # 2 minutes
    ping_interval=60
)


@asynccontextmanager
async def lifespan(app):
    pass


def create_app():
    app=FastAPI(
        title="",
        description="API Server For Voice Agent",
        version="1.0.0",
        lifespan=lifespan
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    @app.get("/ping")
    async def ping():
        return {"status" : "pong"}
    return app



app = create_app()
socket_app = socketio.ASGIApp(sio, app)
    

