from hypothesis import given, strategies as st
from agent import simple_calculator


@given(st.integers(), st.integers())
def test_addition(a, b):
    expr = f"{a}+{b}"
    result = simple_calculator(expr)
    assert int(result) == a + b


@given(st.integers(min_value=-100, max_value=100),
       st.integers(min_value=-100, max_value=100)
       )
def test_subtraction(a, b):
    expr = f"{a}-{b}"
    result = simple_calculator(expr)
    assert int(result) == a - b


@given(st.integers(min_value=-50, max_value=50),
       st.integers(min_value=-50, max_value=50)
       )
def test_multiplication(a, b):
    expr = f"{a}*{b}"
    result = simple_calculator(expr)
    assert int(result) == a * b


@given(st.integers(min_value=1, max_value=100),
       st.integers(min_value=1, max_value=100)
       )
def test_division(a, b):
    expr = f"{a}/{b}"
    result = simple_calculator(expr)
    assert abs(float(result) - (a / b)) < 1e-6