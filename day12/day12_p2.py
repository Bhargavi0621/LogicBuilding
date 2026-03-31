"""Print Fibonacci Series:
Write a program to print the Fibonacci series up to a number N entered by the user. 
For example:
Input: Enter the number of terms: 7
Output: Fibonacci series: 0 1 1 2 3 5 8"""

number=int(input("Enter the number of terms: "))
print("Fibonacci series: ", end="")
for i  in range(number):
    if i==0 or i==1:
        print(i, end=" ")
    else:
        a=0
        b=1
        for j in range(2,i+1):
            c=a+b
            a=b
            b=c
        print(c, end=" ")
    
"""python day12_p2.py
Enter the number of terms: 9
Fibonacci series: 0 1 1 2 3 5 8 13 21 """