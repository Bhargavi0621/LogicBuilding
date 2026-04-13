"""Pattern 1:
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""

number=int(input("Enter the number: "))
for i in range(1,number+1):
    k=i%2
    for j in range(1,i+1):
        print(k,end=" ")
        if k==1:
            k=0
        else:
            k=1
    print()

"""python day19_p1.py
Enter the number: 8
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 
"""