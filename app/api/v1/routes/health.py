from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.config import get_settings

router = APIRouter()
settings = get_settings()


@router.get("/")
async def health_check():
    return JSONResponse(
        content={
            "status": "healthy",
            "version": settings.APP_VERSION,
            "name": settings.APP_NAME,
        }
    )
