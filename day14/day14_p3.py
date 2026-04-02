"""Amstrong Number or Not:
Write a program to check if a number is an Armstrong number. For example:
Input: Enter a number: 153
Output: 153 is an Armstrong number."""

number = input("Enter a number: ")
num_digits = len(number)   
armstrong_sum = sum(int(digit) ** num_digits for digit in number)
if armstrong_sum == int(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

"""python day14_p3.py
Enter a number: 370
370 is an Armstrong number."""
