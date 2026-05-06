"""Factorial of a Number
Task: Define a recursive function factorial(n) that returns the product of all positive integers from 1 up to n.
Input: n = 5
Expected Output: 120
"""

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter the positive number: "))
factorial=fact(n)
print(factorial) 

"""python day31_p1.py
Enter the positive number: 8
40320
"""