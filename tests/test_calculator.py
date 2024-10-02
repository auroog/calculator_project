"""
Tests for the calculator module.
"""

import pytest
from faker import Faker
from calculator import Calculator

fake = Faker()

def test_add():
    """Test the add method."""
    calc = Calculator()
    assert calc.add(2, 3) == 5

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
    """Test division by zero raises ValueError."""
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_fake_data_addition():
    """Test the add method with fake data."""
    calc = Calculator()
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    expected_result = a + b
    assert calc.add(a, b) == expected_result
