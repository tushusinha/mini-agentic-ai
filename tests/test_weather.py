import pytest
from agent import get_weather


def test_weather_with_invalid_city():
    result = get_weather("InvalidCity123").lower()
    # It could fail either because of API key or invalid city
    assert "city not found" in result or "invalid api key" in result


@pytest.mark.integration
def test_weather_with_valid_city():
    import os
    if not os.getenv("WEATHER_API_KEY"):
        pytest.skip("Skipping weather test: WEATHER_API_KEY not set")

    result = get_weather("London").lower()
    assert "weather in london" in result or "couldn't fetch weather" in result
