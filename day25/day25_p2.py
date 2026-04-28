"""Check Palindrome
Determine if a string reads the same backward as forward.
Input: "madam"
Output: "Palindrome"
"""

input=input("Enter the string: ").lower()
if input==input[::-1]:
    print("Palindrome")
else:
    print("not Palindrome")

"""python day25_p2.py
Enter the string: Malayalam
Palindrome"""