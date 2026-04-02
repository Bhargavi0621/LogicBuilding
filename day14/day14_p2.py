"""Write a Program to Display All Factors of a Number:
Write a program to find and print all factors of a number entered by the user. For example:
Input: Enter a number: 28
Output: Factors of 28: 1, 2, 4, 7, 14, 28 """

number = int(input("Enter a number: "))
factors = []
for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)
print(f"Factors of {number}: {', '.join(map(str, factors))}")

"""python day14_p2.py
Enter a number: 36
Factors of 36: 1, 2, 3, 4, 6, 9, 12, 18, 36"""