"""Matrix Addition
Add two matrices of the same dimensions.
Input: 
A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
Output:
[[6, 8], [10, 12]]
"""

rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
matrix1=[]
matrix2=[]
result=[]
print("Matrix 1")
for i in range(0,rows):
    r=list(map(int,input(f"Enter the {columns} elements of {i+1}th row: ").split()))
    matrix1.append(r)

print("Matrix 2")
for i in range(0,rows):
    r=list(map(int,input(f"Enter the {columns} elements of {i+1}th row: ").split()))
    matrix2.append(r)

print("Matrix 1",matrix1)
print("Matrix 2",matrix2)
for i in range(0,rows):
    row=[]
    for j in range(0,columns):
        row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row)

print("Result",result)

"""python day28_p3.py
Enter the number of rows: 2
Enter the number of columns: 2
Matrix 1
Enter the 2 elements of 1th row: 5 9
Enter the 2 elements of 2th row: 2 6
Matrix 2
Enter the 2 elements of 1th row: 1 7
Enter the 2 elements of 2th row: 3 2
Matrix 1 [[5, 9], [2, 6]]
Matrix 2 [[1, 7], [3, 2]]
Result [[6, 16], [5, 8]]
"""