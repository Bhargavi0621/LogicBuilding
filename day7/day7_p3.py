"""Pattern 3: Inverted traingle
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *"""

number=int(input("Enter an odd number: "))
for i in range((number+1)//2):
    for j in range(i):
        print("  ",end="")
    for k in range(number-i*2):
        print("* ",end="")
    print()

"""python day7_p3.py
Enter an odd number: 11
* * * * * * * * * * * 
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *"""