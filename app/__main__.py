import uvicorn
from fastapi import FastAPI

from app.api import activity_router, building_router, organizations_router
from app.settings import app_settings
from app.utils.exception_handler import register_exception_handlers

app = FastAPI(title="RestAPI Test Task")
register_exception_handlers(app)

routers = [activity_router, building_router, organizations_router]
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "app.__main__:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=False,
    )
