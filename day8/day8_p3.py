"""Pattern 9
1 2 3 4 5  
1 2 3 4  
1 2 3  
1 2  
1  """

number=int(input("Enter the number: "))
for i in range(number):
    for j in range(number-i):
        print(j+1," ",end="")
    print()

"""python day8_p3.py
Enter the number: 7
1  2  3  4  5  6  7  
1  2  3  4  5  6
1  2  3  4  5
1  2  3  4
1  2  3
1  2
1 """