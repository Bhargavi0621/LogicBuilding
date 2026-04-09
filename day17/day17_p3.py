"""Pattern - 2
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""

number=int(input("Enter the number: "))
for i in range(1,int(number//2)+2):
    print("  "*(int(number//2)-i+1)+"* "*(2*i-1))
for i in range(int(number//2),0,-1):
    print("  "*(int(number//2)-i+1)+"* "*(2*i-1))

"""python day17_p3.py
Enter the number: 15
              * 
            * * * 
          * * * * * 
        * * * * * * * 
      * * * * * * * * * 
    * * * * * * * * * * * 
  * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * 
    * * * * * * * * * * * 
      * * * * * * * * * 
        * * * * * * * 
          * * * * * 
            * * * 
              * 
              """