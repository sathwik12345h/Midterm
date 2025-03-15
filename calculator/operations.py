"""
Module providing basic arithmetic operations.
"""

from decimal import Decimal

def add(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Returns the sum of two operands."""
    return operand1 + operand2

def subtract(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Returns the difference of two operands."""
    return operand1 - operand2

def multiply(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Returns the product of two operands."""
    return operand1 * operand2

def divide(operand1: Decimal, operand2: Decimal) -> Decimal:
    """Returns the quotient of two operands. Raises an error if dividing by zero."""
    if operand2 == 0:
        raise ValueError("Cannot divide by zero.")
    return operand1 / operand2
