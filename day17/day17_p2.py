"""Pattern - 1
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

number=int(input("Enter number: "))
for i in range(1,number+1):
    print("* "*i)
for i in range(number-1,0,-1):
    print("* "*i)

"""python day17_p2.py
Enter number: 6
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""
