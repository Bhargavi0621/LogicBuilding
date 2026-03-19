"""Print the Multiplication Table of a Given Number:
Write a program where the user enters a number, and the program prints its multiplication table. For example:
Input: Enter a number: 5
Output:
5 x 1 = 5
5 x 2 = 10
5 x 10 = 50"""
number=int(input("Enter a number:"))
for i in range(1,11):
    print(number," x ", i,"=",number*i)
"""python day4_p1.py
Enter a number:7
7  x  1 = 7
7  x  2 = 14
7  x  3 = 21
7  x  4 = 28
7  x  5 = 35
7  x  6 = 42
7  x  7 = 49
7  x  8 = 56
7  x  9 = 63
7  x  10 = 70"""
