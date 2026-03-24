"""Pattern 1: Inverted Right-angled triangle
* * * * *
* * * *
* * *
* *
*"""

number=int(input("Enter a number: "))
for i in range(number):
    for j in range(number-i):
        print("* ",end="")
    print()

"""python day7_p1.py
Enter a number: 8
* * * * * * * * 
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*"""