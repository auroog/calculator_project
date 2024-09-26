class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    @staticmethod
    def to_float(value: str) -> float:
        """Convert a string to a float."""
        try:
            return float(value)
        except ValueError:
            raise ValueError("Invalid input; please enter a numeric value.")

    @classmethod
    def from_history(cls, history: list) -> 'Calculator':
        """Create a calculator instance with a pre-defined history."""
        calc = cls()
        calc.history = history
        return calc
