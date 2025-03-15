# pylint: disable=all

"""
Unit tests for arithmetic operations.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    """Test addition operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15')

def test_operation_subtract():
    """Test subtraction operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5')

def test_operation_multiply():
    """Test multiplication operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50')

def test_operation_divide():
    """Test division operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2')

def test_divide_by_zero():
    """Ensure division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculation(Decimal('10'), Decimal('0'), divide).perform()

def test_operation(a, b, operation, expected):# pylint: disable=invalid-name
    '''Testing various operations'''
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"
     