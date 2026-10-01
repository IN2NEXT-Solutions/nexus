from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.errors import register_exception_handlers
from app.core.logging import configure_logging


configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for IN2NEXT Nexus.",
)

register_exception_handlers(app)

app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["system"])
async def root() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "status": "ok",
    }
