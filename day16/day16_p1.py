"""Write a Program to Check Whether a Number is a Palindrome:
Write a program to determine if a number is a palindrome. 
For example:
Input: Enter a number: 121
Output: 121 is a palindrome."""

number=input("Enter a number: ")
if number==number[::-1]:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

"""python day16_p1.py
Enter a number: 454
454 is a palindrome."""