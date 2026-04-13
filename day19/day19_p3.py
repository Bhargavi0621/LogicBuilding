"""Pattern 3:
E
D E
C D E
B C D E
A B C D E
"""

number=int(input("Enter the number: "))
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(number,0,-1):
    for j in range(i,number+1):
        print(alpha[j-1],end=" ")
    print()

"""python day19_p3.py
Enter the number: 8
H 
G H 
F G H 
E F G H 
D E F G H 
C D E F G H 
B C D E F G H 
A B C D E F G H """