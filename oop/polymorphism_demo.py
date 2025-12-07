# polymorphism_demo.py
import math

class Shape:
    def area(self):
        # Must be overridden by subclasses
        raise NotImplementedError("area() must be implemented by subclasses")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Keep as int when inputs are ints to match expected "50" (not 50.0)
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Use math.pi as required
        return math.pi * (self.radius ** 2)