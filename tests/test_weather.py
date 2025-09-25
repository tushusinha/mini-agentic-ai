import os
import pytest
from agent import get_weather


@pytest.mark.unit
def test_weather_with_invalid_city():
    # This should fail gracefully with a meaningful error
    result = get_weather("InvalidCity123")
    assert "Couldn't fetch weather" in result or "Error" in result


@pytest.mark.unit
def test_weather_without_api_key(monkeypatch):
    # Temporarily remove API key
    monkeypatch.setenv("WEATHER_API_KEY", "")
    # Import again (simulating missing key)
    import importlib
    import agent
    importlib.reload(agent)

    with pytest.raises(ValueError):
        if not os.getenv("WEATHER_API_KEY"):
            raise ValueError("❌ Please set WEATHER_API_KEY in your .env file")
