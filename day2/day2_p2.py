"""Program to Check Whether the Number is Divisible by 5:
Write a program that determines if a number entered by the user is divisible by 5. For example:
Input: Enter a number: 25
Output: 25 is divisible by 5"""
#take input from user
number = int(input("Enter the number: "))
#check if the number is divisible by 5
if number % 5 == 0:
    print(number, "is divisible by 5")
else:
    print(number, "is not divisible by 5")

"""Output:
python day2_p2.py
Enter the number: 557
557 is not divisible by 5"""