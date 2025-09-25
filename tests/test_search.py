import pytest
from agent import search_duckduckgo


@pytest.mark.integration
def test_search_real_duckduckgo():
    """Integration test: hits DuckDuckGo search API."""
    query = "latest AI news"
    result = search_duckduckgo(query)
    assert isinstance(result, str)
    assert len(result) > 0


@pytest.mark.unit
def test_search_returns_string():
    result = search_duckduckgo("OpenAI GPT-5")
    assert isinstance(result, str)
