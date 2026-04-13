"""Pattern - 2
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
"""

number=int(input("Enter the number: "))
for i in range(1,(number*2)+1):
    if i==1 or i==(number*2):
        print("* "*number*2)
    elif i<=number:
        print("* "*(number-(i-1)),"  "*(2*(i-1)-1),"* "*(number-(i-1)))
    else:
        print("* "*(i-number),"  "*(((number-(i-number))*2)-1),"* "*(i-number))

"""python day18_p2.py
Enter the number: 7
* * * * * * * * * * * * * * 
* * * * * *     * * * * * * 
* * * * *         * * * * * 
* * * *             * * * * 
* * *                 * * * 
* *                     * * 
*                         * 
*                         * 
* *                     * * 
* * *                 * * * 
* * * *             * * * * 
* * * * *         * * * * * 
* * * * * *     * * * * * * 
* * * * * * * * * * * * * * 
"""