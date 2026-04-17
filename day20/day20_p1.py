"""Pattern 1
   *
  * *
 *   *
*     *
 *   *
  * *
   *
"""

number=int(input("Enter the number: "))
for i in range(1,number*2):
    if i<number+1:
        for j in range(1,number*2):
            if j==number-i+1 or j==number+i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
    elif i>number:
        for j in range(1,number*2):
            if j==i-number+1 or j==(number*2)-(i-number+1):
                print("*",end="")
            else:
                print(" ",end="")
        print()

"""python day20_p1.py
Enter the number: 6
     *     
    * *    
   *   *   
  *     *  
 *       * 
*         *
 *       * 
  *     *  
   *   *   
    * *    
     *   
"""