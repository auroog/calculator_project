"""
This module provides basic calculator operations
"""

import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
LOG_LEVEL = os.getenv("Log_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL)



class Calculator:
    """A class for performing basic arithmetic operations."""

    @staticmethod
    def add(num1, num2):
        """Return the sum of num1 and num2."""
        result = num1 + num2
        logging.debug("Adding %s + %s = %s", num1, num2, result)
        return result

    @staticmethod
    def subtract(num1, num2):
        """Return the difference of num1 and num2."""
        result = num1 - num2
        logging.debug("Subtracting %s - %s = %s", num1, num2, result)
        return result

    @staticmethod
    def multiply(num1, num2):
        """Return the product of num1 and num2."""
        result = num1 * num2
        logging.debug("Multiplying %s * %s = %s", num1, num2, result)
        return result

    @staticmethod
    def divide(num1, num2):
        """Return the quotient of num1 and num2. Raises ValueError if num2 is zero."""
        if num2 == 0:
            logging.error("Attempted division by zero")
            raise ValueError("Cannot divide by zero.")
        result = num1 / num2
        logging.debug("Dividing %s / %s = %s", num1, num2, result)
        return result
