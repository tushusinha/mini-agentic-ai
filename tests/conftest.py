import pytest


@pytest.fixture(autouse=True)
def fake_env(monkeypatch):
    """Provide fake API keys during tests to avoid import errors."""
    monkeypatch.setenv("OPENAI_API_KEY", "fake-openai-key")
    monkeypatch.setenv("WEATHER_API_KEY", "fake-weather-key")
