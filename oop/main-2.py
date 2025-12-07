# main.py
from class_static_methods_demo import Calculator

if __name__ == "__main__":
    s = Calculator.add(7, 8)       # 15
    print(f"The sum is: {s}")

    p = Calculator.multiply(10, 5) # prints the calculation type, then returns 50
    print(f"The product is: {p}")