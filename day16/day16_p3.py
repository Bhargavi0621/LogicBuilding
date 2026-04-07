"""Print All Digits and Alphabets Using a For Loop:
Write a program to print all digits (0–9) and alphabets (A–Z, a–z) using a for loop. 
For example:
Output:
Digits: 0 1 2 3 4 5 6 7 8 9
Alphabets: A B C ... Z a b c ... z
"""

print("Digits: ",end="")
for i in range(0,10):
    print(i,end=" ")
print()
print("Alphabets: ",end="")
for i in range(65,91):
    print(chr(i),end=" ")
for i in range(97,123):
    print(chr(i),end=" ")

"""python day16_p3.py
Digits: 0 1 2 3 4 5 6 7 8 9 
Alphabets: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z """