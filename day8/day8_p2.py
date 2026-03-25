"""Pattern 8
1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5  """

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(0,i+1):
        print(i+1," ",end="")
    print()

"""python day8_p2.py
Enter the number: 8
1  
2  2
3  3  3
4  4  4  4
5  5  5  5  5
6  6  6  6  6  6
7  7  7  7  7  7  7
8  8  8  8  8  8  8  8 """