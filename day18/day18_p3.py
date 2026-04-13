"""Pattern - 3
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

number=int(input("Enter the number: "))
k=1
for i in range(1,number+1):
        for j in range(1,i+1):
                print(k,end=" ")
                k=k+1
        print()

"""python day18_p3.py
Enter the number: 8
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 32 33 34 35 36 """