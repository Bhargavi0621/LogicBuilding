"""Write a Program to Find the Largest Number Among Three Numbers:
Write a program where the user enters three numbers, and the program finds and displays the largest number among them. 
For example:
Input: Enter three numbers: 12, 25, 7
Output: The largest number is: 25"""

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
if num1>num2:
    large=num1
else :
    large=num2
if num3>large:
    large=num3
print("The largest number is: ",large)

"""python day11_p1.py
Enter the first number: 23
Enter the second number: 55
Enter the third number: 98
The largest number is:  98"""