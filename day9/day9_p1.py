"""Pattern 1
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
"""

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(i+1):
        print(j+1," ",end="")
    for k in range(2*(number-i-1)):
        print("   ",end="")
    for j in range(i+1):
        print(i-j+1," ",end="")
    print()
        
    """python day9_p1.py
Enter the number: 5
1                          1  
1  2                    2  1
1  2  3              3  2  1
1  2  3  4        4  3  2  1
1  2  3  4  5  5  4  3  2  1 """