"""Program to Check Whether the Number is Odd or Even:
Write a program that checks whether a number entered by the user is odd or even. For example:
Input: Enter a number: 7
Output: 7 is an odd number"""

#take input from user
number = int(input("Enter the number: "))
#check odd or even and print the number
if number % 2 == 0:
    print(number, "is an even number")
else:    
    print(number, "is an odd number")
"""Output:
python day2_p1.py
Enter the number: 21
21 is an odd number"""