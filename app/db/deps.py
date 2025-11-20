from app.db.session import AsyncSessionLocal
from contextlib import asynccontextmanager

@asynccontextmanager
async def get_session():
    async with AsyncSessionLocal() as session:
        async with session.begin():
           yield session