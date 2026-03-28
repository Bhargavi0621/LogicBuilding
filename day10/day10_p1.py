"""Pattern 1
A
B B
C C C
D D D D
E E E E E"""

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(i+1):
        print(chr(65+i)," ",end="")
    print()

""" python day10_p1.py
Enter the number: 8
A  
B  B  
C  C  C  
D  D  D  D
E  E  E  E  E
F  F  F  F  F  F
G  G  G  G  G  G  G
H  H  H  H  H  H  H  H """