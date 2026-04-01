"""Write a Program to Calculate the Power of a Number:
Write a program that takes a base and an exponent as input and calculates the power of the base raised to the exponent using both manual calculation and the pow() function. For example:
Input: Base: 2, Exponent: 3
Output:
Result using manual calculation: 8
Result using pow(): 8"""

def manual_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result  
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))   
manual_result = manual_power(base, exponent)
pow_result = pow(base, exponent)
print(f"Result using manual calculation: {manual_result}")
print(f"Result using pow(): {pow_result}")
"""python day13_p2.py
Enter the base: 4 
Enter the exponent: 3
Result using manual calculation: 64.0
Result using pow(): 64.0"""