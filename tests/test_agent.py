import os
import pytest
from agent import run_agent


@pytest.mark.integration
def test_agent_math_query():
    result = run_agent("What is 2+2?")
    assert "4" in result


@pytest.mark.integration
def test_agent_weather_query():
    # Run only if WEATHER_API_KEY is available
    if not os.getenv("WEATHER_API_KEY"):
        pytest.skip("Skipping weather test: WEATHER_API_KEY not set")
    result = run_agent("What is the weather in London?")
    assert "Weather in London" in result or "Couldn't fetch weather" in result


@pytest.mark.integration
def test_agent_file_reader(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello from test!")

    query = f"Read the file at {file_path}"
    result = run_agent(query)
    assert "Hello from test!" in result


@pytest.mark.integration
def test_agent_search_query():
    result = run_agent("Summarize OpenAI's latest research")
    assert isinstance(result, str)
    assert len(result) > 0
