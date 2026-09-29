"""Calculator management for the command-line application."""

from app.calculation import CalculationFactory


class Calculator:
    """Manage calculations and calculation history."""

    def __init__(self):
        """Initialize an empty calculation history."""
        self.history = []

    def calculate(self, operation_name: str, a: float, b: float) -> float:
        """Create, perform, and store a calculation."""
        calculation = CalculationFactory.create_calculation(
            operation_name,
            a,
            b
        )

        result = calculation.perform()
        self.history.append(calculation)

        return result

    def get_history(self):
        """Return the calculation history."""
        return self.history

    def clear_history(self):
        """Clear all stored calculations."""
        self.history.clear()