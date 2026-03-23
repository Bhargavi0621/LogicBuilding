"""Pattern 3: Hallow Rectangle
* * * * *
*       *
*       *
*       *
* * * * *"""

number=int(input("Enter the number: "))
for i in range(1,number+1):
    for j in range(1,number+1):
        if i==1 or j==1 or j==number or i==number:
            print("* ",end="")
        else:
                print("  ",end="")
    print()

"""python day6_p3.py
Enter the number: 6
* * * * * * 
*         *
*         *
*         *
*         *
* * * * * *"""