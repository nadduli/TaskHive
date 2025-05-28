from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from .i18n import get_locale


class LocaleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Store the locale in request state
        request.state.locale = get_locale(request)
        response = await call_next(request)
        return response
