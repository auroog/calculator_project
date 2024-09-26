class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def __init__(self):
	"""Initialize the calculator with an empty history."""
        self.history = []

    def add(self, a: float, b: float) -> float:
	"""Return the sum of a and b, and log the operation in history."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the subtraction of a and b, and log the operation in history."""
	result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the multiplication of a and b, and log the operation in history."""
	result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Return the division of a and b, and log the operation in history."""
	if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        return self.history

    @staticmethod
    def to_float(value: str) -> float:
        """Convert a string to a float."""
        try:
            return float(value)
        except ValueError as exc:
            raise ValueError("Invalid input; please enter a numeric value.") from exc

    @classmethod
    def from_history(cls, history: list) -> 'Calculator':
        """Create a calculator instance with a pre-defined history."""
        calc = cls()
        calc.history = history
        return calc
