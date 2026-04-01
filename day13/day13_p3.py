"""Result using pow(): 8
Program to Print Integers in Words:
Write a program that converts each digit of an integer entered by the user into its corresponding word representation. For example:
Input: Enter a number: 123
Output: One Two Three"""

def digit_to_word(digit):
    words = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    return words.get(digit, '')

number = input("Enter a number: ")
words = [digit_to_word(digit) for digit in number]
print(" ".join(words))

"""python day13_p3.py   
Enter a number: 216
Two One Six"""