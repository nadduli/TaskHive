#!/usr/bin/python3
"""My test file"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}