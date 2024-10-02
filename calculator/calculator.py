"""This module contains the Calculator class with static methods for arithmetic operations."""
class Calculator:
    """A class for performing basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Return the quotient of a and b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
