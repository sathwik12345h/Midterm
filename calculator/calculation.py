"""
Module defining the Calculation class for executing arithmetic operations.
"""

from decimal import Decimal
from typing import Callable

class Calculation:
    """Encapsulates an arithmetic operation with two operands."""

    def __init__(self, operand1: Decimal, operand2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initializes a calculation with two operands and an operation."""
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation

    @staticmethod
    def create(operand1: Decimal, operand2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Creates and returns a new Calculation object."""
        return Calculation(operand1, operand2, operation)

    def perform(self) -> Decimal:
        """Performs the arithmetic operation and returns the result."""
        return self.operation(self.operand1, self.operand2)

    def __repr__(self):
        """Provides a readable string representation of the calculation."""
        return f"Calculation({self.operand1}, {self.operand2}, {self.operation.__name__})"
