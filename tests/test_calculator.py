"""Tests for the Calculator class."""

from app.calculator import Calculator


def test_calculator_add():
    """Test performing an addition calculation."""
    calculator = Calculator()

    result = calculator.calculate("add", 2, 3)

    assert result == 5


def test_calculator_history():
    """Test that completed calculations are stored in history."""
    calculator = Calculator()

    calculator.calculate("add", 2, 3)
    calculator.calculate("multiply", 4, 5)

    history = calculator.get_history()

    assert len(history) == 2
    assert history[0].perform() == 5
    assert history[1].perform() == 20


def test_clear_history():
    """Test clearing the calculation history."""
    calculator = Calculator()

    calculator.calculate("add", 2, 3)

    assert len(calculator.get_history()) == 1

    calculator.clear_history()

    assert calculator.get_history() == []
