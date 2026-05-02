"""Search an Element in a Matrix
Search for a given element in a matrix and return its position.
Input:
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], Target = 5
Output:
Position: (1, 1) (0-based index)
"""

r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
matrix=[]
print("Matrix:")
for i in range(0,r):
    row=[]
    for j in range(0,c):
        e=int(input(f"Enter the element [{i}][{j}]: "))
        row.append(e)
    matrix.append(row)

target=int(input("Enter the Target: "))
print("Matrix: ",matrix)
print("Target: ",target)
for i in range(0,r):
    for j in range(0,c):
        if matrix[i][j]==target:
            position=(i,j)
            break
print("Position: ",position)

"""python day29_p2.py
Enter the number of rows: 3
Enter the number of columns: 4
Matrix:
Enter the element [0][0]: 2       
Enter the element [0][1]: 3
Enter the element [0][2]: 5
Enter the element [0][3]: 7
Enter the element [1][0]: 1
Enter the element [1][1]: 9
Enter the element [1][2]: 8
Enter the element [1][3]: 23
Enter the element [2][0]: 57
Enter the element [2][1]: 18
Enter the element [2][2]: 22
Enter the element [2][3]: 33
Enter the Target: 18
Matrix:  [[2, 3, 5, 7], [1, 9, 8, 23], [57, 18, 22, 33]]
Target:  18
Position:  (2, 1)
"""