"""Longest Word in a Sentence
Find the longest word in a given sentence.
Input: "The quick brown fox"
Output: "quick"
"""

sentence=input("Enter the sentence: ")
array=sentence.split()
max=0
for i in array:
    if len(i)>max:
        max=len(i)
        word=i
print(word) 

"""python day26_p1.py
Enter the sentence: Hello my name is Bhargavi
Bhargavi"""
