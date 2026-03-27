"""Pattern 3
A B C D E
A B C D
A B C
A B
A
"""

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(number-i):
        print(chr(65+j)," ",end="")
    print()

"""python day9_p3.py 
Enter the number: 8
A  B  C  D  E  F  G  H  
A  B  C  D  E  F  G
A  B  C  D  E  F
A  B  C  D  E
A  B  C  D
A  B  C
A  B
A """