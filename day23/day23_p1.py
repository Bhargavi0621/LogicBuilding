"""Find the Missing Number in an Array
Given an array of numbers from 1 to n with one number missing, find the missing number.
Input: [1, 2, 4, 5, 6]
Output: Missing Number: 3
"""

array=[int(x) for x in input("Enter the array: ").split()]
for i in range(0,len(array)):
    if array[i]!=i+1:
        print("Missing Number: ",i+1)
        break

"""python day23_p1.py
Enter the array: 1 2 3 4 5 7 8 9 10
Missing Number:  6
"""