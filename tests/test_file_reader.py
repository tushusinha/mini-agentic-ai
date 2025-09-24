import tempfile
import pytest
from safe_utils import read_file

@pytest.mark.unit
def test_file_reader_valid():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write("Hello, world!")
        tmp.flush()
        path = tmp.name

    content = read_file(path)
    assert "Hello, world!" in content

@pytest.mark.unit
def test_file_reader_invalid_path():
    result = read_file("non_existent_file.txt")
    assert "Error reading file" in result