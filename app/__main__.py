from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

import uvicorn
from fastapi import FastAPI

from app.database.bootstrap import drop_database, init_database
from app.settings import app_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:  # noqa
    await init_database()
    yield
    if app_settings.env == "dev":
        await drop_database()  # for early dev purposes only


app = FastAPI(lifespan=lifespan, title="MedianBonus")

routers = []
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "backend.__main__:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=False,
    )
