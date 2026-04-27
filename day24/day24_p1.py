"""Find the Second Largest Element in an Array
Find the second largest element in the array.
Input: [10, 20, 4, 45, 99]
Output: Second Largest: 45
"""

array=[int (x) for x in input("Enter the elements of the array: ").split()]
array.sort()
print("Second Largest: ",array[-2])

""" python day24_p1.py
Enter the elements of the array: 3 45 24 78 56 98
Second Largest:  78"""