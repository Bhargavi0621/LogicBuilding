"""Factorial of a Number Using a For Loop:
Write a program to calculate the factorial of a number entered by the user using a for loop. 
For example:
Input: Enter a number: 4
Output: Factorial of 4 is 24."""

number=int(input("Enter a number: "))
for i in range(1,number+1):
    if i==1:
        factorial=1 
    else:
        factorial=i*factorial
print(f"Factorial of {number} is {factorial}")

"""python day12_p1.py
Enter a number: 6
Factorial of 6 is 720"""