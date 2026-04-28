"""Find All Substrings of a String
Print all possible substrings of a string.
Input: "abc"
Output: ["a", "b", "c", "ab", "bc", "abc"]
"""

word=input("Enter the word: ")
result=[]
for i in range(0,len(word)):
    for j in range(i+1,len(word)+1):
        result.append(word[i:j])
print(result)

"""python day26_p3.py
Enter the word: jam
['j', 'ja', 'jam', 'a', 'am', 'm']
"""