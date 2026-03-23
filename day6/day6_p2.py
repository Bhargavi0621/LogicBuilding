"""Pattern 2: Right-angled trinagle
*
* *
* * *
* * * *
* * * * *"""

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(i+1):
        print("* ", end="")
    print()

"""python day6_p2.py
Enter the number: 6
* 
* *
* * *
* * * *
* * * * *
* * * * * *"""