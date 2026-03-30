"""Write a Program to Check Whether a Year Entered by the User is a Leap Year:
Write a program to determine whether a given year is a leap year. For example:
Input: Enter a year: 2024
Output: 2024 is a leap year."""

year=int(input("Enter a year: "))
if year%100==0:
    if year%400==0:
        print(year," is a leap year.")
    else:
        print(year," is not a leap year.")  
elif year%4==0:
    print(year," is a leap year.`")
else:
    print(year," is not a leap year.")

"""python day11_p2.py
Enter a year: 1700 
1700  is not a leap year."""