"""This module contains the main logic for the interactive calculator."""

import logging
from decimal import Decimal, InvalidOperation
import os
import importlib
from multiprocessing import Process
from faker import Faker
from dotenv import load_dotenv
from calculator import Calculator

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()

environment = os.getenv('ENVIRONMENT')
api_key = os.getenv('API_KEY')

print(f"Environment: {environment}")
print(f"API Key: {api_key}")

fake = Faker()

def load_plugins():
    """Load plugins from the specified folder."""
    plugins = {}
    plugin_folder = 'plugins'
    for filename in os.listdir(plugin_folder):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module = importlib.import_module(f"{plugin_folder}.{module_name}")
            plugins[module_name] = module
            logging.info("Loaded plugin: %s", module_name)
    return plugins

def calculate_and_print(num1, num2, operation_name):
    """Calculate and print the result of the specified operation."""
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        if operation_name == 'divide' and num2 == Decimal('0'):
            raise ZeroDivisionError

        num1_decimal, num2_decimal = map(Decimal, [num1, num2])
        result_function = operation_mappings.get(operation_name)

        if result_function:
            result = result_function(num1_decimal, num2_decimal)
            logging.info(f"The result of {num1} {operation_name} {num2} is {result}")
            return f"The result of {num1} {operation_name} {num2} is equal to {result}"
        else:
            logging.warning(f"Unknown operation: {operation_name}")
            return f"Unknown operation: {operation_name}"
    except (InvalidOperation, ValueError):
        logging.error(f"Invalid number input: {num1} or {num2} is not a valid number.")
        return f"Invalid number input: {num1} or {num2} is not a valid number."
    except ZeroDivisionError:
        logging.error("Error: Division by zero.")
        return "Error: Division by zero."

def main():
    """Main function to run the calculator."""
    while True:
        command = input("Enter command (add, subtract, multiply, divide, or 'exit' to quit): ")
        if command == 'exit':
            logging.info("Exiting the calculator.")
            break
        process_command(command)

def process_command(command):
    """Process user commands for calculations."""
    if command in ['add', 'subtract', 'multiply', 'divide']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculate_and_print(num1, num2, command)
            print(result)
        except ValueError as error:
            logging.error("Invalid input: %s", error)
            print("Invalid input. Please enter valid numbers.")
    elif command == 'menu':
        display_menu()
    else:
        print("Unknown command. Type 'menu' to see available commands.")

def display_menu():
    """Display available commands for the Calculator."""
    logging.info("\nAvailable commands:")
    logging.info("add - Add two numbers")
    logging.info("subtract - Subtract two numbers")
    logging.info("multiply - Multiply two numbers")
    logging.info("divide - Divide two numbers")
    logging.info("exit - Exit the program")

if __name__ == "__main__":
    main()
