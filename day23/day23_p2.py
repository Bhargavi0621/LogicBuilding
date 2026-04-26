"""Find the Majority Element in an Array
Find the element that appears more than n/2 times in the array (if any).
Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
Output: Majority Element: 4
"""

array=[int(x) for x in input("Enter the elements of the array: ").split()]
lenght=len(array)
array.sort()
count=1
found=False
for i in range(1,lenght):
    if array[i]==array[i-1]:
        count+=1
    else:
        if count>lenght//2:
            print(f"Majority Element: {array[i-1]}")
            found=True
            break
        count=1
if not found:
    if count>lenght//2:
        print(f"Majority Element: {array[-1]}")
    else:
        print("Majority Element not there ")

""" python day23_p2.py
Enter the elements of the array: 3 3 4 3 4 3 3 7 8 3 9 3 9    
Majority Element: 3
"""