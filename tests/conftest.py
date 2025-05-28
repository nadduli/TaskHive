#!/usr/bin/python3
"""Test configuration and fixtures"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)


@pytest.fixture
def test_headers():
    """Headers fixture for different locales"""
    return {
        "en": {"Accept-Language": "en"},
        "es": {"Accept-Language": "es"},
        "fr": {"Accept-Language": "fr"},  # Unsupported language
        "complex": {"Accept-Language": "en-US,en;q=0.9,es;q=0.8"},
    }
