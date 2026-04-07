"""Print Factorial Series:
Write a program that prints the factorial of numbers from 1 to N, where the user enters N. 
For example:
Input: Enter a number: 5
Output:
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
"""

number=int(input("Enter a number: "))
fact=1
for i in range(1,number+1):
    fact=fact*i
    print(i,"!=",fact)

"""day15_p3.py
Enter a number: 7
1 != 1
2 != 2
3 != 6
4 != 24
5 != 120
6 != 720
7 != 5040"""