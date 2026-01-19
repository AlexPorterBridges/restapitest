from .base import Base
from .session import engine


# for early dev purposes only
async def init_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# for early dev purposes only
async def drop_database() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
