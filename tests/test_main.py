#!/usr/bin/python3
"""Test module for the main application"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Health check endpoint called",
        "data": {"status": "OK"},
        "status_code": 200,
    }


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the API",
        "data": {"URL": ""},
        "status_code": 200,
    }
