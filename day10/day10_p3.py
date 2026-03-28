"""Program to Perform Swapping of Two Numbers:
Write a program to swap two numbers entered by the user. For example:
Input: Enter first number: 10, Enter second number: 20
Output:
    Before swapping: a = 10, b = 20
    After swapping: a = 20, b = 10"""

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("Before swapping: a=",num1,", b=",num2)
temp=num1
num1=num2
num2=temp
print("After swapping: a=",num1,", b=",num2)

"""python day10_p3.py
Enter the first number: 21
Enter the second number: 3
Before swapping: a= 21 , b= 3
After swapping: a= 3 , b= 21"""