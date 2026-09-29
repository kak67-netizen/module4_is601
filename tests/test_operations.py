"""Tests for arithmetic operation classes."""

import pytest

from app.operation import Add, Subtract, Multiply, Divide, Operation


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Add(), 2, 3, 5),
        (Add(), -1, 1, 0),
        (Subtract(), 10, 4, 6),
        (Subtract(), 3, 5, -2),
        (Multiply(), 4, 5, 20),
        (Multiply(), -2, 3, -6),
        (Divide(), 10, 2, 5),
        (Divide(), 7, 2, 3.5),
    ],
)
def test_operations(operation, a, b, expected):
    """Test arithmetic operations with multiple values."""
    assert operation.execute(a, b) == expected


def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ZeroDivisionError):
        Divide().execute(10, 0)


def test_base_operation_not_implemented():
    """Test that the base Operation class cannot execute directly."""
    with pytest.raises(NotImplementedError):
        Operation().execute(1, 2)