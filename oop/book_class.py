for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
 # polymorphism_demo.py
import math

class Shape:
    """Base class for all shapes."""
    
    def area(self):
        """Method to calculate the area, should be overridden in derived classes."""
        raise NotImplementedError("This method should be overridden by subclasses.")


class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, length: float, width: float):
        """Initialize a Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, radius: float):
        """Initialize a Circle instance with radius."""
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)   
    # main.py

from class_static_methods_demo import Shape, Rectangle, Circle

def main():
    # Create a list of shapes
    shapes = [
        Rectangle(10, 5),  # Rectangle with length 10 and width 5
        Circle(7)          # Circle with radius 7
    ]

    # Print the area of each shape
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()