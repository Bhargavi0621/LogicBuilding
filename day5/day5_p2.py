"""Write a Program to Check Whether a Character is a Vowel or Consonant:
Write a program to check whether a character entered by the user is a vowel (a, e, i, o, u) or a consonant. For example:
Input: Enter a character: e
Output: e is a vowel."""
vowels=("a","e","i","o","u")
character=input("Enter a character:")
if character.lower() in (vowels):
    print(character,"is a vowel.")
else:
    print(character,"is a consonant.")

"""python day5_p2.py
Enter a character:I
I is a vowel."""