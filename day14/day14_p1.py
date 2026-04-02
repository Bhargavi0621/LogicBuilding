"""Print Numbers in Words in Reverse Order Using a Switch Case:
Write a program that takes an integer, reverses it, and prints each digit as a word using a switch case. For example:
Input: Enter a number: 321
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
reversed_number = number[::-1]
words = [digit_to_word(digit) for digit in reversed_number] 
print(" ".join(words))

"""python day14_p1.py
Enter a number: 247
Seven Four Two"""