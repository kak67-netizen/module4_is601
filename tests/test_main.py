"""Tests for the calculator command-line interface."""

from app.main import get_number, run_calculator


def test_get_number_valid(monkeypatch):
    """Test entering a valid number."""
    monkeypatch.setattr("builtins.input", lambda _: "5")

    assert get_number("Enter number: ") == 5.0


def test_get_number_invalid_then_valid(monkeypatch, capsys):
    """Test invalid numeric input followed by valid input."""
    inputs = iter(["abc", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_number("Enter number: ")

    captured = capsys.readouterr()

    assert result == 7.0
    assert "Invalid number. Please try again." in captured.out


def test_repl_help_and_exit(monkeypatch, capsys):
    """Test help and exit commands."""
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    captured = capsys.readouterr()

    assert "Available commands:" in captured.out
    assert "Goodbye!" in captured.out


def test_repl_invalid_command(monkeypatch, capsys):
    """Test an invalid command."""
    inputs = iter(["power", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    captured = capsys.readouterr()

    assert "Invalid command. Type 'help' for options." in captured.out


def test_repl_empty_history(monkeypatch, capsys):
    """Test viewing history before calculations are performed."""
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    captured = capsys.readouterr()

    assert "No calculations in history." in captured.out


def test_repl_calculation_and_history(monkeypatch, capsys):
    """Test performing a calculation and viewing history."""
    inputs = iter([
        "add",
        "2",
        "3",
        "history",
        "exit",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    captured = capsys.readouterr()

    assert "Result: 5.0" in captured.out
    assert "2.0 Add 3.0 = 5.0" in captured.out


def test_repl_divide_by_zero(monkeypatch, capsys):
    """Test division-by-zero handling in the REPL."""
    inputs = iter([
        "divide",
        "10",
        "0",
        "exit",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_calculator()

    captured = capsys.readouterr()

    assert "Error: Cannot divide by zero." in captured.out