from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import settings


router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@router.get("", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=settings.app_name.lower().replace(" ", "-"),
        version=settings.app_version,
    )
