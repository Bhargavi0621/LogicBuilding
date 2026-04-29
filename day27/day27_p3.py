"""Remove All Non-Alphabetic Characters
Remove all characters that are not letters.
Input: "abc123!@#"
Output: "abc"
"""

string=input("Enter the string: ")
result=""
for i in (string):
    if i.isalpha():
        result+=i
print(result) 

"""python day27_p3.py
Enter the string: asdf1234!@#$fghj&*()45fg
asdffghjfg
"""