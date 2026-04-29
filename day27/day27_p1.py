"""Check Anagrams
Determine if two strings are anagrams of each other.
Input: "listen", "silent"
Output: "Anagrams"
"""

word1=input("Enter the firs word: ").lower()
word2=input("Enter the second word: ").lower()
w1="".join(sorted(word1))
w2="".join(sorted(word2))
if w1==w2:
    print("Anagrams")
else:
    print("Not Anagrams")

"""python day27_p1.py
Enter the firs word: Race
Enter the second word: Care
Anagrams"""
