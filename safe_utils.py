import math


def simple_calculator(expression: str) -> str:
    try:
        return str(eval(expression, {"__builtins__": None, "math": math}))
    except Exception as e:
        return f"Error: {str(e)}"


def read_file(filepath: str) -> str:
    try:
        with open(filepath, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"
