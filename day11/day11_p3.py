"""Write a Program to Calculate the Sum of the First N Natural Numbers:
Write a program where the user enters a number N, and the program calculates the sum of all natural numbers up to N.
 For example:
Input: Enter a number: 5
Output: The sum of the first 5 natural numbers is 15."""

number=int(input("Enter the number: "))
sum=int(number*(number+1)/2)
print("The sum of the first",number,"natural numbers is ",sum)

"""python day11_p3.py
Enter the number: 8
The sum of the first 8 natural numbers is  36"""