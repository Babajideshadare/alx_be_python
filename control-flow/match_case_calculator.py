# match_case_calculator.py
num1 = float(input("Enter the first number: ")) # using float to allow decimal numbers
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.") 
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Error: Invalid operation selected.")