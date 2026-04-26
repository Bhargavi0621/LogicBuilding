"""Reverse an Array
Reverse the order of elements in the given array.
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""

array=[int(x) for x in input("Enter the elements of the array: ").split()]
print(array[::-1])

"""python day23_p3.py
Enter the elements of the array: 3 5 6 7 8 9
[9, 8, 7, 6, 5, 3]"""