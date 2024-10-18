"""
Tests for the main module of the calculator application.
"""

import logging
import pytest
from main import calculate_and_print

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def test_calculate_and_print():
    logging.debug("Testing addition")
    assert calculate_and_print(5, 3, 'add') == "The result of 5 add 3 is equal to 8"

    logging.debug("Testing subtraction")
    assert calculate_and_print(10, 2, 'subtract') == "The result of 10 subtract 2 is equal to 8"

    logging.debug("Testing multiplication")
    assert calculate_and_print(4, 5, 'multiply') == "The result of 4 multiply 5 is equal to 20"

    logging.debug("Testing division")
    assert calculate_and_print(20, 4, 'divide') == "The result of 20 divide 4 is equal to 5"

    logging.debug("Testing division by zero")
    assert calculate_and_print(1, 0, 'divide') == "Error: Division by zero."

    logging.debug("Testing unknown operation")
    assert calculate_and_print(9, 3, 'unknown') == "Unknown operation: unknown"

    logging.debug("Testing invalid input 'a'")
    assert calculate_and_print('a', 3, 'add') == "Invalid number input: a or 3 is not a valid number."

    logging.debug("Testing invalid input 'b'")
    assert calculate_and_print(5, 'b', 'subtract') == "Invalid number input: 5 or b is not a valid number."
