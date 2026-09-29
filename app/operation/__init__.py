"""Arithmetic operation classes for the calculator."""


class Operation:
    """Base class for arithmetic operations."""

    def execute(self, a: float, b: float) -> float:
        """Perform an arithmetic operation."""
        raise NotImplementedError("Subclasses must implement execute().")


class Add(Operation):
    """Add two numbers."""

    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    """Subtract the second number from the first."""

    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    """Multiply two numbers."""

    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    """Divide the first number by the second."""

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b