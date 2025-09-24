import pytest
from safe_utils import simple_calculator

@pytest.mark.unit
def test_calculator_addition():
    assert simple_calculator("2+3") == "5"

@pytest.mark.unit
def test_calculator_with_math_module():
    assert simple_calculator("math.sqrt(16)") == "4.0"

@pytest.mark.unit
def test_calculator_invalid_expression():
    result = simple_calculator("2/0")
    assert "Error" in result