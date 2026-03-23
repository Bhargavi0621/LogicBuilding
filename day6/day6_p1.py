"""Pattern 1: Sqaure
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *"""

number=int(input("Enter the number: "))
for i in range(number):
    for i in range(number):
       print("* ",end="")
    print()

""" python day6_p1.py 
Enter the number6
* * * * * * 
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *"""