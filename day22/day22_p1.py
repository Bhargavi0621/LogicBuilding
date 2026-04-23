"""Print the Array in Sorted Order (Ascending and Descending):
Write a program to sort an array in ascending and descending order. For example:
Input: [5, 3, 8, 1]
Output:
Ascending: [1, 3, 5, 8]
Descending: [8, 5, 3, 1]
"""

Array=[int(x) for x in input("Enter the elements of array: ").split()]
print("Original array: ",Array)
for i in range(0,len(Array)):
    for j in range(0,len(Array)-i-1):
        if Array[j]>Array[j+1]:
            tem=Array[j]
            Array[j]=Array[j+1]
            Array[j+1]=tem
print("After sort array: ",Array)
print("After sort array: ",Array[::-1])

"""python day22_p1.py
Enter the elements of array: 9 4 8 7 1 5 3 21 6
Original array:  [9, 4, 8, 7, 1, 5, 3, 21, 6]
After sort array:  [1, 3, 4, 5, 6, 7, 8, 9, 21]
After sort array:  [21, 9, 8, 7, 6, 5, 4, 3, 1]
"""