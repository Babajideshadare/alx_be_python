# main.py
from polymorphism_demo import Rectangle, Circle

if __name__ == "__main__":
    rect = Rectangle(10, 5)   # 10 * 5 = 50
    circ = Circle(7)          # pi * 7^2 = 153.93804002589985

    print(f"The area of the Rectangle is: {rect.area()}")
    print(f"The area of the Circle is: {circ.area()}")