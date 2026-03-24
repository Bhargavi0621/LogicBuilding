"""Pattern 2: traingle
       *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *"""

number=int(input("Enter an odd number: "))
for i in range((number+1)//2):
    for j in range(number//2-i):
        print("  ",end="")
    for k in range(2*i+1):
        print("* ",end="")
    print()
    
"""python day7_p2.py
Enter an odd number: 11
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *"""   