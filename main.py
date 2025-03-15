# pragma: no cover
"""
Command-line interface for performing basic calculator operations.
"""

from calculator import Calculator
from decimal import Decimal, InvalidOperation
from app import App

def calculate_and_print(operand1, operand2, operation_name):
    """
    Performs the specified arithmetic operation and prints the result.

    Args:
        operand1 (str): First number as a string (to be converted to Decimal).
        operand2 (str): Second number as a string (to be converted to Decimal).
        operation_name (str): The operation to perform (add, subtract, multiply, divide).
    """
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        # Convert input strings to Decimal
        operand1_decimal, operand2_decimal = map(Decimal, [operand1, operand2])

        if operation_name in operation_mappings:
            result = operation_mappings[operation_name](operand1_decimal, operand2_decimal)
            print(f"The result of {operand1} {operation_name} {operand2} is equal to {result}")
        else:
            print(f"Error: Unsupported operation '{operation_name}'. Available operations: add, subtract, multiply, divide.")

    except InvalidOperation:
        print(f"Invalid number input: {operand1} or {operand2} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    # """
    # Parses command-line arguments and executes the requested operation.
    # """
    # if len(sys.argv) != 4:
    #     print(f"Usage: python {sys.argv[0]} <number1> <number2> <operation>")
    #     print("Example: python main.py 10 5 add")
    #     sys.exit(1)

    # _, operand1, operand2, operation = sys.argv
    # calculate_and_print(operand1, operand2, operation)
    app = App()  # Initialize the App class
    app.start()

if __name__ == '__main__':
    main()
