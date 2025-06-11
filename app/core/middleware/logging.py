#!/usr/bin/python3
"""Request logging middleware"""

import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging HTTP requests"""

    async def dispatch(self, request: Request, call_next):
        """Log request and response details"""
        start_time = time.time()

        logger.info(f"Request started: {request.method} {request.url.path}")

        try:
            response = await call_next(request)
            process_time = (time.time() - start_time) * 1000

            logger.info(
                f"Request completed: {request.method} {request.url.path} - "
                f"Status: {response.status_code} - "
                f"Duration: {process_time:.2f}ms"
            )
            return response

        except Exception as exc:
            logger.exception(
                f"Request failed: {request.method} {request.url.path} - "
                f"Error: {str(exc)}"
            )
            raise
