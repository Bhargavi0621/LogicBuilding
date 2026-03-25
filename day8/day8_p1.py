"""Pattern 7:
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  """

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(i+1):
        print(j+1," ",end="")
    print()

"""python day8_p1.py
Enter the number: 8
1  
1  2
1  2  3
1  2  3  4
1  2  3  4  5
1  2  3  4  5  6
1  2  3  4  5  6  7
1  2  3  4  5  6  7  8"""