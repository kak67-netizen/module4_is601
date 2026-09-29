"""Tests for Calculation and CalculationFactory."""

import pytest

from app.calculation import Calculation, CalculationFactory
from app.operation import Add


@pytest.mark.parametrize(
    "operation_name,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 10, 4, 6),
        ("multiply", 4, 5, 20),
        ("divide", 10, 2, 5),
    ],
)
def test_calculation_factory(operation_name, a, b, expected):
    """Test factory-created calculations."""
    calculation = CalculationFactory.create_calculation(
        operation_name,
        a,
        b
    )

    assert calculation.perform() == expected


def test_calculation_string():
    """Test readable calculation output."""
    calculation = Calculation(2, 3, Add())

    assert str(calculation) == "2 Add 3 = 5"


def test_factory_case_insensitive():
    """Test that operation names are case-insensitive."""
    calculation = CalculationFactory.create_calculation(
        "ADD",
        2,
        3
    )

    assert calculation.perform() == 5


def test_factory_invalid_operation():
    """Test invalid operation handling."""
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation(
            "power",
            2,
            3
        )