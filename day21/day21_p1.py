"""Perfect Number Write a program to determine if a number is a perfect number.

Input: number = 6
Output: Perfect Number
Explanation: 6 is a perfect number because its divisors (1, 2, 3) sum up to 6.
"""

number=int(input("Enter the number: "))
sum=0
for i in range(1,int(number/2)+1):
    if number%i==0:
        sum=sum+i
if number==sum:
    print("Perfect Number")
else:
    print("Not Perfect Number")

"""python day21_p1.py
Enter the number: 28
Perfect Number
python day21_p1.py
Enter the number: 38
Not Perfect Number"""