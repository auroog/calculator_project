from calculator import Calculator
from decimal import Decimal, InvalidOperation
from faker import Faker 

fake = Faker()

def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        if operation_name == 'divide' and b == "0":
            raise ZeroDivisionError

        a_decimal, b_decimal = map(Decimal, [a, b])
        result_function = operation_mappings.get(operation_name)
        if result_function:
            result = result_function(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except (InvalidOperation, ValueError):
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

print(fake.name())
print(fake.address())
