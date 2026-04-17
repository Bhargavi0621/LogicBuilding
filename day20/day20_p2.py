"""Pattern 2
    1
  1 2 1
1 2 3 2 1
"""

number=int(input("Enter the number: "))
for i in range(1,number+1):
    k=1
    m=2
    print("  "*(number-i),end="")
    for j in range(1,i*2):
        if k<=i:
            print(k,end=" ")
            k=k+1
        else:
            print(k-m,end=" ")
            m=m+1
    print()

"""python day20_p2.py
Enter the number: 5    
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
"""
