"""Check if Two Strings are Rotations of Each Other
Check if one string is a rotation of another.
NOTE : the order of characters matters in rotations.
Input: "abcd", "cdab"
Output: "Yes"
"""

word1=input("Enter the first string: ")
word2=input("Enter the second string: ")
if len(word1)!=len(word2):
    print("No")
else:
        if word2 in word1+word1:
            print("Yes")
        else:
            print("No")

"""python day27_p2.py
Enter the first string: dfghjk
Enter the second string: ghjkdf
Yes
"""