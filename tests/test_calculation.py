# pylint: disable=all

"""
Unit tests for the Calculation class in the calculator module.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, divide

def test_calculation_operations(a, b, operation, expected):
    """
    Test arithmetic operations with Decimal operands and ensure Calculation 
    class returns expected results.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} with {a} and {b}"

def test_calculation_repr():
    """
    Test the __repr__ method for accurate object representation.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "Incorrect repr output."

def test_divide_by_zero():
    """
    Ensure dividing by zero raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
        