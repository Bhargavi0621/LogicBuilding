"""Matrix Transpose
Find the transpose of a matrix (convert rows to columns and vice versa).
Input:
A = [[1, 2, 3], [4, 5, 6]]
Output:
[[1, 4], [2, 5], [3, 6]]
"""

r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
matrix=[]
transpose=[]
print("Matrix:")
for i in range(0,r):
    row=[]
    for j in range(0,c):
        e=int(input(f"Enter the element [{i}][{j}]: "))
        row.append(e)
    matrix.append(row)

for i in range(0,c):
    row=[]
    for j in range(0,r):
        e=matrix[j][i]
        row.append(e)
    transpose.append(row)
print("Matrix: ",matrix)
print("Transpose: ",transpose)

"""python day29_p3.py
Enter the number of rows: 3
Enter the number of columns: 4
Matrix:
Enter the element [0][0]: 1
Enter the element [0][1]: 2
Enter the element [0][2]: 3
Enter the element [0][3]: 4
Enter the element [1][0]: 5
Enter the element [1][1]: 6
Enter the element [1][2]: 7
Enter the element [1][3]: 8
Enter the element [2][0]: 9
Enter the element [2][1]: 10
Enter the element [2][2]: 11
Enter the element [2][3]: 12
Matrix:  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Transpose:  [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
"""