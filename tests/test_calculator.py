import pytest
from calculator import Calculator 

def test_add():
	"""Test the add method."""
	calc = Calculator()
	assert calc.add(2,3) == 5

def test_subtract():
	"""Test the subtraction method."""
	calc = Calculator()
	assert calc.subtract(10, 5) == 5

def test_multiply():
	"""Test the multiplication method."""
	calc = Calculator()
	assert calc.multiply(4, 5) == 20

def test_divide():
	"""Test the division method."""
	calc = Calculator()
	assert calc.divide(10, 2) == 5

def test_divide_by_zero():
	calc = Calculator()
	with pytest.raises(ValueError):
		calc.divide(10,0)

def test_to_float_valid():
	assert Calculator.to_float("3.14") == 3.14

def test_to_float_invalid():
	with pytest.raises(ValueError):
		Calculator.to_float("invalid")

def test_from_history():
    history = ["2 + 3 = 5", "10 - 5 = 5"]
    calc = Calculator.from_history(history)
    assert calc.history == history

def test_history():
    calc = Calculator()
    calc.add(1, 2)
    calc.subtract(5, 3)
    assert len(calc.history) == 2
    assert calc.history[-1] == "5 - 3 = 2"
