"""
Calculator module that provides arithmetic operations and history management.
"""

from decimal import Decimal
from typing import Callable

from calculator.calculation_history import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    """Handles core calculator operations and maintains history."""

    @staticmethod
    def _perform_operation(
        operand1: Decimal, operand2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]
    ) -> Decimal:
        """Executes an arithmetic operation and stores it in history."""
        calculation = Calculation.create(operand1, operand2, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(operand1: Decimal, operand2: Decimal) -> Decimal:
        """Returns the sum of two operands."""
        return Calculator._perform_operation(operand1, operand2, add)

    @staticmethod
    def subtract(operand1: Decimal, operand2: Decimal) -> Decimal:
        """Returns the difference between two operands."""
        return Calculator._perform_operation(operand1, operand2, subtract)

    @staticmethod
    def multiply(operand1: Decimal, operand2: Decimal) -> Decimal:
        """Returns the product of two operands."""
        return Calculator._perform_operation(operand1, operand2, multiply)

    @staticmethod
    def divide(operand1: Decimal, operand2: Decimal) -> Decimal:
        """Returns the quotient of two operands. Raises an error if dividing by zero."""
        return Calculator._perform_operation(operand1, operand2, divide)
