# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two values with error handling.

    Returns:
        str: Either an error message or 'Result: <value>'.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return "Error: Please provide two numeric inputs."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Format to 2 decimal places; adjust if your checker expects full precision
    return f"Result: {result:.2f}"