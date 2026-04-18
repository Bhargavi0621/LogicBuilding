"""Largest Prime Factor Write a program to find the largest prime factor of a given number.

Input: number = 28
Output: 7
"""
def isprime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True

number=int(input("Enter the number: "))
p=number
for i in range(int(number/2),1,-1):
    if isprime(i) and number%i==0:
        p=i
        break
print(p)

"""python day21_p2.py
Enter the number: 78
13"""
    
