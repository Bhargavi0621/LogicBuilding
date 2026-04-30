"""
Count Vowels and Consonants
Count the number of vowels and consonants in a string.
Input: "hello"
Output: Vowels: 2, Consonants: 3
"""

word=input("Enter the string: ").lower()
vowels=['a','e','i','o','u']
vowel=0
consonant=0
for i in word:
    if i in vowels:
        vowel+=1
    else:
        consonant+=1
print(f"Vowels: {vowel} Consonants:{consonant}")

"""python day28_p2.py
Enter the string: Bhargavi
Vowels: 3 Consonants:5"""