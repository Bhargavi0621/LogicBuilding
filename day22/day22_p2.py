"""Finding the Longest Sequence of Consecutive 1s in a Binary Array
Write a program to find the longest sequence of consecutive 1s in a binary array.
Input: binaryArray = [1, 1, 0, 1, 1, 1]
Output: 3
"""

binarray=[int(x) for x in input("Enter the binary Array: ").split()]
count=0
max=0
for i in range(0,len(binarray)):
    if binarray[i]==1:
        count=count+1
        if count>max:
            max=count
    else:
        count=0
print(f"longest sequence of consecutive 1's is {max}")

"""python day22_p2.py
Enter the binary Array: 1 1 0 0 1 0 1 1 1 1 1 0 1
longest sequence of consecutive 1's is 5"""