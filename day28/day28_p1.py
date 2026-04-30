"""Find Duplicate Characters in a String
Identify all characters that appear more than once in a string.
Input: "programming"
Output: ["r", "g", "m"]
"""

from collections import defaultdict
word=input("Enter the word: ").lower()
w="".join(sorted(word))
result=defaultdict(int)
count=1
for i in range(1,len(word)):
    if w[i]==w[i-1]:
        count+=1
        result[w[i]]=count
    else:
        count=1
key=list(result.keys())
print(key)
        
""" 
python day28_p1.py
Enter the word: Statistics 
['i', 's', 't']
"""