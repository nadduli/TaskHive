#!/usr/bin/python3
"""Auth Route module"""

from app.core.security import create_access_token, hash_password
from app.services.auth_service import get_google_user, oauth
from fastapi.responses import RedirectResponse
from app.core.config import get_settings
from fastapi import Depends, Request, APIRouter


router = APIRouter()
settings = get_settings()


@router.get("/google/login")
async def google_login(request: Request):
    """login with google"""
    redirect_url = settings.GOOGLE_REDIRECT_URI
    return await oauth.google.authorize_redirect(request, redirect_url)


@router.get("/google/callback")
async def google_callback(request: Request):
    user = await get_google_user(request)
    access_token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {"email": user.email, "name": user.full_name, "picture": user.picture},
    }

