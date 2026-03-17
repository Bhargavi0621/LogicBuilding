"""Program to Check Whether the Number is a Multiple of 7:
Write a program that verifies if a number entered by the user is a multiple of 7. For example:
Input: Enter a number: 14
Output: 14 is a multiple of 7."""
#take input from user
number = int(input("Enter the number: "))
#check if the number is a multiple of 7
if number % 7 == 0:
    print(number, "is a multiple of 7")
else:
    print(number, "is not a multiple of 7")

"""Output:
python day2_p3.py
Enter the number: 42
42 is a multiple of 7"""