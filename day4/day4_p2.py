"""Write a Program to Make a Simple Calculator Using a Switch Case:
Write a program that acts as a calculator, taking two numbers and an operator (+, -, *, /) from the user, and performing the operation based on the operator. For example:
Input: Enter first number: 10, Operator: +, Second number: 20
Output: 10 + 20 = 30"""
num1=float(input("Enter first number: "))
Operator=(input("Operator: "))
num2=float(input("Second number: "))
match Operator:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator")
"""python day4_p2.py
Enter first number: 45
Operator: -
Second number: 16
45.0 - 16.0 = 29.0"""