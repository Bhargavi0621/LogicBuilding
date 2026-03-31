"""Write a Program to Find the GCD or HCF of Two Numbers:
Write a program where the user enters two numbers, and the program calculates their greatest common divisor (GCD) or highest common factor (HCF). 
For example:
Input: Enter two numbers: 60, 48
Output: The GCD of 60 and 48 is 12."""

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1 < num2:
    smaller = num1
else:
    smaller = num2
for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i

print(f"The GCD of {num1} and {num2} is {gcd}")

"""python day12_p3.py
Enter the first number: 48
Enter the second number: 76
The GCD of 48 and 76 is 4"""