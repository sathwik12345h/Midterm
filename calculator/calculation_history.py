"""
Module for managing a history of calculations.
"""

from typing import List
from calculator.calculation import Calculation

class Calculations:
    """Manages the history of performed calculations."""

    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Returns the full calculation history."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clears all stored calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Retrieves the most recent calculation. Returns None if history is empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Finds all calculations matching a given operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
