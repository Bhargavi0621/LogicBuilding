"""Matrix Multiplication
Multiply two matrices if the number of columns in the first matrix equals the number of rows in the second.
Input:
A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
Output:
[[19, 22], [43, 50]]
"""

r1=int(input("Enter the number of rows in first matrix: "))
c1=int(input("Enter the number of columns in first matrix: "))
r2=int(input("Enter the number of rows in second matrix: "))
c2=int(input("Enter the number of columns in second matrix: "))

if c1!=r2:
    print("The number of columns in the first matrix is not equal to the number of rows in the second matrix.")
else:
    matrix1=[]
    matrix2=[]
    result=[]
    print("Matrix 1")
    for i in range(0,r1):
        row=[]
        for j in range(0,c1):
            e=int(input(f"Enter the [{i}][{j}] element: "))
            row.append(e)
        matrix1.append(row)

    print("Matrix 2")
    for i in range(0,r2):
        row=[]
        for j in range(0,c2):
            e=int(input(f"Enter the [{i}][{j}] element: "))
            row.append(e)
        matrix2.append(row)
    
    for i in range(0,r1):
        row=[]
        for j in range(0,c2):
            sum=0
            for k in range(0,r2):
                sum=sum+(matrix1[i][k]*matrix2[k][j])
            row.append(sum)
        result.append(row)
    print("Result")
    print(matrix1,"X",matrix2,"=",result)

"""python day29_p1.py
Enter the number of rows in first matrix: 3 
Enter the number of columns in first matrix: 2
Enter the number of rows in second matrix: 2
Enter the number of columns in second matrix: 4
Matrix 1
Enter the [0][0] element: 3
Enter the [0][1] element: 4
Enter the [1][0] element: 7
Enter the [1][1] element: 2
Enter the [2][0] element: 5
Enter the [2][1] element: 9
Matrix 2
Enter the [0][0] element: 3
Enter the [0][1] element: 1
Enter the [0][2] element: 5
Enter the [0][3] element: 7
Enter the [1][0] element: 6 
Enter the [1][1] element: 9
Enter the [1][2] element: 2
Enter the [1][3] element: 5
Result
[[3, 4], [7, 2], [5, 9]] X [[3, 1, 5, 7], [6, 9, 2, 5]] = [[33, 39, 23, 41], [33, 25, 39, 59], [69, 86, 43, 80]]
"""