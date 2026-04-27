"""Remove Duplicates from an Array
Remove all duplicates from the given array and return the unique elements..
Input: [1, 2, 2, 3, 4, 1, 5]
Output: [1, 2, 3, 4, 5]
"""

array=[int (x) for x in input("Enter the elements of the array: ").split()]
array.sort()
result=[]
for i in array:
    if i not in result:
        result.append(i)
print(result)

"""python day24_p2.py
Enter the elements of the array: 2 4 5 2 8 5 9 4 6 3 3 2 6 
[2, 3, 4, 5, 6, 8, 9]"""