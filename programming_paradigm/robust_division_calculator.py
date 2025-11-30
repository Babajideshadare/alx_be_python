# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two values with error handling.

    Returns:
        str: Error message or 'The result of the division is <value>'.
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

    # Use Python's default float representation to match checker output
    return f"The result of the division is {result}"