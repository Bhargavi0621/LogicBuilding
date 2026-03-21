"""Calculate the Sum of Digits of a Given Number:
Write a program that calculates the sum of the digits of a number entered by the user. For example:
Input: Enter a number: 1234
Output: Sum of digits: 10"""

number=int(input("Enter a number:"))
sum=0
while number>0:
    rem=number%10
    sum+=rem
    number=int(number/10)
print("Sum of digits:",sum)

"""python day5_p1.py
Enter a number:2103
Sum of digits: 6"""