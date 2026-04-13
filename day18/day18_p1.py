"""Pattern - 1
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                  *
"""

number=int(input("Enter the number: "))
for i in range(1,number*2):
    if i<number:
        print("* "*i,"  "*(2*(number-i)-1),"* "*i)
    elif i==number:
        print("* "*(number*2))
    else:
        print("* "*(number-(i-number)),"  "*(2*(i-number)-1),"* "*(number-(i-number)))

"""python day18_p1.py
Enter the number: 7
*                         * 
* *                     * * 
* * *                 * * * 
* * * *             * * * * 
* * * * *         * * * * * 
* * * * * *     * * * * * * 
* * * * * * * * * * * * * * 
* * * * * *     * * * * * * 
* * * * *         * * * * * 
* * * *             * * * * 
* * *                 * * * 
* *                     * * 
*                         *
 """