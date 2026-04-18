"""Sum of the series of n terms Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.

Input: n = 4
Output: 2.083333
"""
number=int(input("Enter the number: "))
sum=0
for i in range(1,number+1):
    sum=sum+(1/i)
print(f"{sum: .6f}")

"""python day21_p3.py
Enter the number: 8
 2.717857"""