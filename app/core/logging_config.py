#!/usr/bin/python3
"""Logging configuration module"""

import sys
import logging
from loguru import logger


class InterceptHandler(logging.Handler):
    """Intercepts standard logging and redirects to loguru"""

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging():
    """Configure logging for development environment"""
    logger.remove()

    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan> | "
        "<level>{message}</level>"
    )

    logger.add(sys.stderr, format=log_format, level="DEBUG", colorize=True)

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    for logger_name in ["uvicorn", "uvicorn.access", "sqlalchemy.engine"]:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler()]
