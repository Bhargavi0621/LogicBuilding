"""Write a Program to Find the LCM of Two Numbers:
Write a program where the user enters two numbers, and the program calculates their least common multiple (LCM). 
For example:
Input: Enter two numbers: 4, 6
Output: The LCM of 4 and 6 is 12."""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a  

def lcm(a, b):
    return (a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))  
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {result}.")
"""python day13_p1.py
Enter the first number: 8
Enter the second number: 14
The LCM of 8 and 14 is 56."""