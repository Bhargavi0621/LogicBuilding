""" Power of a Number
Task: Write a recursive function power(base, exponent) to calculate the value of a base raised to a specific power.
Input: base = 2, exponent = 3
Expected Output: 8 
"""

def power(base,expo):
    if expo==1:
        return base
    return base*power(base,expo-1)

base=int(input("Enter base: "))
expo=int(input("Enter exponent: "))
result=power(base,expo)
print(result)

"""python day31_p2.py
Enter base: 4
Enter exponent: 2
16"""