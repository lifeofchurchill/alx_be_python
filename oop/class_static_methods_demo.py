class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, c):
        """Print calculation type and return the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * c
