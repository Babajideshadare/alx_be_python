# class_static_methods_demo.py

class Calculator:
    # Class attribute (accessed by class methods via cls)
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # No access to class or instance state
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Access to class state; prints the calculation type before multiplying
        print(f"Calculation type: {cls.calculation_type}")
        return a * b