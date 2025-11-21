from app.db.session import AsyncSessionLocal
from contextlib import asynccontextmanager

#helper for creating session basically nothing much (dependecy injection)
@asynccontextmanager
async def get_async_session():
    async with AsyncSessionLocal() as session:
        async with session.begin():
           yield session