@staticmethod
def add(a, b):
    return a + b

@classmethod
def multiply(cls, a, b):
    print(f"Calculation type: {cls.calculation_type}")
    return a * b
# Using the class method
product_result = Calculator.multiply(10, 5)
print(f"The product is: {product_result}")
# class_static_methods_demo.py

class Calculator:
    """A simple calculator class to demonstrate class and static methods."""
    
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    # main.py

from polymorphism import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()