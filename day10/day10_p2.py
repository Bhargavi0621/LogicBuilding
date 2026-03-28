"""Pattern 2
     A
    A B A
  A B C B A
A B C D C B A"""

number=int(input("Enter the number: "))
for i in range(number):
    for n in range(number-i-1):
        print("  ",end="")
    for j in range(i+1):
        print(chr(65+j),"",end="")
    for k in range(i-1,-1,-1):
        print(chr(65+k),"",end="")
    print()

"""python day10_p2.py
Enter the number: 6
          A 
        A B A
      A B C B A
    A B C D C B A
  A B C D E D C B A
A B C D E F E D C B A """