# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two values with error handling.

    Returns:
        str: Either an error message or 'Result: <value>'.
    """
    # Convert inputs to floats, handling non-numeric values
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Perform the division, handling division by zero
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"Result: {result}"