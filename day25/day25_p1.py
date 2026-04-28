"""Find the Frequency of Each Element in an Array
Calculate the frequency of each element in the array.
Input: [1, 2, 2, 3, 1, 4, 5, 1]
Output: {1: 3, 2: 2, 3: 1, 4: 1, 5: 1}
"""
from collections import defaultdict
freq=defaultdict(int)
array=[int(x) for x in input("Enter the elements of the array : ").split()]
array.sort()
for i in array:
    freq[i]+=1
print(dict(freq))

"""python day25_p1.py
Enter the elements of the array : 5 3 8 5 9 3 6 5 6 5 5 3
{3: 3, 5: 5, 6: 2, 8: 1, 9: 1}
"""