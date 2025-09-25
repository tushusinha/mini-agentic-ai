import pytest
from agent import search_duckduckgo


@pytest.mark.unit
def test_search_returns_string():
    result = search_duckduckgo("OpenAI GPT-5")
    assert isinstance(result, str)
    assert len(result) > 0
