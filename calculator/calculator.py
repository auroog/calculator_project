import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure logging to output to a file or console based on environment
env = os.getenv("ENVIRONMENT", "development")  # Default to development if ENVIRONMENT not set
log_level = logging.DEBUG if env == "development" else logging.INFO

# Configure logging
logging.basicConfig(level=log_level, filename="logs/app.log" if env == "production" else None,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info(f"Running in {env} environment")


class Calculator:
    """A class for performing basic arithmetic operations."""

    @staticmethod
    def add(num1, num2):
        """Return the sum of num1 and num2."""
        result = num1 + num2
        logging.debug(f"Adding {num1} + {num2} = {result}")
        return result

    @staticmethod
    def subtract(num1, num2):
        """Return the difference of num1 and num2."""
        result = num1 - num2
        logging.debug(f"Subtracting {num1} - {num2} = {result}")
        return result

    @staticmethod
    def multiply(num1, num2):
        """Return the product of num1 and num2."""
        result = num1 * num2
        logging.debug(f"Multiplying {num1} * {num2} = {result}")
        return result

    @staticmethod
    def divide(num1, num2):
        """Return the quotient of num1 and num2. Raises ValueError if num2 is zero."""
        if num2 == 0:
            logging.error("Attempted division by zero")
            raise ValueError("Cannot divide by zero.")
        result = num1 / num2
        logging.debug(f"Dividing {num1} / {num2} = {result}")
        return result
