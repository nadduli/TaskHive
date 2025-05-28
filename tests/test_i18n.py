#!/usr/bin/python3
"""Tests for the internationalization (i18n) functionality"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.i18n import t, get_locale
from fastapi import Request

client = TestClient(app)


def test_welcome_endpoint_english():
    """Test welcome endpoint with English language header"""
    response = client.get("/welcome", headers={"Accept-Language": "en"})
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TaskHive", "locale": "en"}


def test_welcome_endpoint_spanish():
    """Test welcome endpoint with Spanish language header"""
    response = client.get("/welcome", headers={"Accept-Language": "es"})
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a TaskHive", "locale": "es"}


def test_welcome_endpoint_default_locale():
    """Test welcome endpoint with no language header"""
    response = client.get("/welcome")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TaskHive", "locale": "en"}


def test_welcome_endpoint_unsupported_locale():
    """Test welcome endpoint with unsupported language"""
    response = client.get("/welcome", headers={"Accept-Language": "fr"})
    assert response.status_code == 200
    # Should fall back to English
    assert response.json() == {"message": "Welcome to TaskHive", "locale": "fr"}


def test_translation_function():
    """Test the translation function directly"""
    # Test English translations
    assert t("common.welcome", locale="en") == "Welcome to TaskHive"
    assert t("task.create", locale="en") == "Create Task"
    assert t("user.login", locale="en") == "Login"

    # Test Spanish translations
    assert t("common.welcome", locale="es") == "Bienvenido a TaskHive"
    assert t("task.create", locale="es") == "Crear Tarea"
    assert t("user.login", locale="es") == "Iniciar Sesión"


def test_get_locale_function():
    """Test the get_locale function"""
    # Test with English header
    mock_request = Request({"type": "http", "headers": [(b"accept-language", b"en")]})
    assert get_locale(mock_request) == "en"

    # Test with Spanish header
    mock_request = Request({"type": "http", "headers": [(b"accept-language", b"es")]})
    assert get_locale(mock_request) == "es"

    # Test with complex Accept-Language header
    mock_request = Request(
        {"type": "http", "headers": [(b"accept-language", b"en-US,en;q=0.9")]}
    )
    assert get_locale(mock_request) == "en"

    # Test with no header
    mock_request = Request({"type": "http", "headers": []})
    assert get_locale(mock_request) == "en"


def test_nested_translations():
    """Test nested translation keys"""
    # Test English nested translations
    assert t("task.status.pending", locale="en") == "Pending"
    assert t("task.status.in_progress", locale="en") == "In Progress"
    assert t("common.error.not_found", locale="en") == "Resource not found"

    # Test Spanish nested translations
    assert t("task.status.pending", locale="es") == "Pendiente"
    assert t("task.status.in_progress", locale="es") == "En Progreso"
    assert t("common.error.not_found", locale="es") == "Recurso no encontrado"


def test_translation_with_params():
    """Test translations with parameter interpolation"""
    # Add a new test key to both language files first
    from pathlib import Path
    import json

    # Update English translations
    en_file = Path("app/translations/en.json")
    es_file = Path("app/translations/es.json")

    for file_path in [en_file, es_file]:
        with open(file_path, "r+") as f:
            data = json.load(f)
            if file_path == en_file:
                data["common"]["hello_user"] = "Hello, %{name}!"
            else:
                data["common"]["hello_user"] = "¡Hola, %{name}!"
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

    # Test parameter interpolation
    assert t("common.hello_user", locale="en", name="John") == "Hello, John!"
    assert t("common.hello_user", locale="es", name="John") == "¡Hola, John!"
