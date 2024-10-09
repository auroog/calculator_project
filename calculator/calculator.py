"""This module contains the Calculator class with static methods for arithmetic operations."""
class Calculator:
    """A class for performing basic arithmetic operations."""

    @staticmethod
    def add(num1, num2):
        """Return the sum of a and b."""
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        """Return the difference of a and b."""
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        """Return the product of a and b."""
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        """Return the quotient of num1 and num2. Raises ValueError if num2 is zero."""
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
