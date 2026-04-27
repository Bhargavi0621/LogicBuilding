"""Move Zeros to the End of an Array
Move all zeros in the array to the end while maintaining the relative order of non-zero elements.
Input: [0, 1, 2, 0, 3, 4, 0]
Output: [1, 2, 3, 4, 0, 0, 0]
"""

array=[int (x) for x in input("Enter the elements of the array: ").split()]
k=0
count=0
for i in array:
    if i==0:
        count+=1
    else:
        array[k]=i
        k+=1
for i in range(0,count):
    array[k]=0
    k+=1
print(array)

"""python day24_p3.py
Enter the elements of the array: 5 0 3 9 0 4 0 6 7 0 9 
[5, 3, 9, 4, 6, 7, 9, 0, 0, 0, 0]"""