"""Program to Find the Larger Number Among Two Numbers:
Write a program to compare two integers entered by the user and print the larger one. For example:
Input: Enter two numbers: 15, 20 
Output: The larger number is: 20"""

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if num1 > num2:
    print("The larger number is:", num1)
else:
    print("The larger number is:", num2)