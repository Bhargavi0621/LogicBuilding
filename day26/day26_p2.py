"""Find the First Non-Repeating Character
Identify the first character that does not repeat in the string.
Input: "swiss"
Output: "w"
"""

word=input("Enter the word: ").lower()
result=True
for i in range(0,len(word)):
    result=True
    for j in range(0,len(word)):
        if i!=j and word[i]==word[j]:
            result=False
            break
    if result:
        print("The First Non-Repeating Character is ",word[i])
        break

"""python day26_p2.py
Enter the word: Malayalam
The First Non-Repeating Character is  y
"""


