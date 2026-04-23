"""Finding the Most Frequent Element in an Array
Write a program to find the most frequent element in an array.
Input: array = [1, 2, 2, 3, 3, 3]
Output: 3
"""
array=[int(x) for x in input("enter the array: ").split()]
array.sort()
count=0
max=0
num=0
for i in range(1,len(array)):
    if array[i-1]==array[i]:
        count+=1
        if count>max:
            max=count
            num=array[i]
    else:
        count=0
print(f"Most Frequent Element in an Array is {num}")

""" python day22_p3.py
enter the array: 1 5 7 2 9 4 7 4 0 2 4 8 4 9 4 2 4 8 4
Most Frequent Element in an Array is 4 """
