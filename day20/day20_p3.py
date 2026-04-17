"""Pattern 3
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""
number=int(input("Enter the number: "))
for i in range(1, number+1):
    for j in range(1,number+1):
        print((i+j)%2,end=" ")
    print()
