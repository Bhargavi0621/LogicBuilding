"""
Pattern 2:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""
number=int(input("Enter the number: "))
for i in range(1,number*2):
    for j in range(1,number*2):
        if abs(i-number)>abs(j-number):
            k=abs(i-number)+1
        else:
            k=abs(j-number)+1
        print(k,end=" ")
    print()

"""python day19_p2.py
Enter the number: 5
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5 """       