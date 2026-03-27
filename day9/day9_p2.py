"""Pattern 2
A
A B
A B C
A B C D
A B C D E"""

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(i+1):
        print(chr(65+j)," ",end="")
    print()

"""python day9_p2.py
Enter the number: 6
A  
A  B
A  B  C
A  B  C  D
A  B  C  D  E
A  B  C  D  E  F"""    