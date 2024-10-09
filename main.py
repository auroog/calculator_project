"""This module contains the main logic for the interactive calculator."""
from decimal import Decimal, InvalidOperation
import os
import importlib
from multiprocessing import Process
from faker import Faker
from calculator import Calculator

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
    return plugins

def run_add(num1, num2):
    """Perform addition using the Calculator."""
    return num1 + num2

def run_subtract(num1, num2):
    """Perform subtraction using the Calculator."""
    return num1 - num2

def run_multiply(num1, num2):
    """Perform multiplication using the Calculator."""
    return num1 * num2

def run_divide(num1, num2):
    """Perform division using the Calculator."""
    return num1 / num2

def calculate_and_print(num1, num2, operation_name):
    """Calculate and print the result of the specified operation."""
    operation_mappings = {
        'add': run_add,
        'subtract': run_subtract,
        'multiply': run_multiply,
        'divide': run_divide
    }

    try:
        if operation_name == 'divide' and num2 == Decimal('0'):
            raise ZeroDivisionError

        num1_decimal, num2_decimal = map(Decimal, [num1, num2])
        result_function = operation_mappings.get(operation_name)

        if result_function:
            process = Process(target=result_function, args=(num1_decimal, num2_decimal))
            process.start()
            process.join()
            result = result_function(num1_decimal, num2_decimal)
            print(f"The result of {num1} {operation_name} {num2} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except (InvalidOperation, ValueError):
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")

def main():
    """Main function to run the calculator."""
    while True:
        command = input("Enter command (add, subtract, multiply, divide, or 'exit' to quit): ")
        if command == 'exit':
            print("Exiting the calculator")
            break
        process_command(command)

def process_command(command):
    """Process user commands for calculations."""
    if command in ['add', 'subtract', 'multiply', 'divide']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        try:
            if command == 'add':
                result = Calculator.add(num1, num2)
            elif command == 'subtract':
                result = Calculator.subtract(num1, num2)
            elif command == 'multiply':
                result = Calculator.multiply(num1, num2)
            elif command == 'divide':
                result = Calculator.divide(num1, num2)

            print(f"The result is: {result}")
        except ValueError as error:
            print(f"Invalid input: {error}")

    elif command == 'menu':
        display_menu()
    else:
        print("Unknown command. Type 'menu' to see available commands.")

def display_menu():
    """Display available commands for the Calculator."""
    print("\nAvailable commands:")
    print("add - Add two numbers")
    print("subtract - Subtract two numbers")
    print("multiply - Multiply two numbers")
    print("divide - Divide two numbers")
    print("exit - Exit the program")

if __name__ == "__main__":
    main()
