"""Write a Program to Convert Binary Numbers to Decimal and Vice Versa Manually:
Write a program that uses user-defined functions to convert binary numbers to decimal and decimal numbers to binary. For example:
Input: Enter a binary number: 1010
Output: Decimal equivalent: 10
Input: Enter a decimal number: 10
Output: Binary equivalent: 1010"""

def Binary_to_decimal(num):
    sum=0
    j=len(num)-1
    for i in num:
        sum=sum+int(i)*pow(2,j)
        j=j-1
    return sum

def Decimal_to_binary(num):
    binary=""
    while num>0:
        rem=num%2
        num=int(num/2)
        binary+=str(rem)
    return binary[::-1]

binary=input("Enter a binary number: ")
dec=Binary_to_decimal(binary)
print("Decimal equivalent: ",dec)
decimal=int(input("Enter a decimal number: "))
bina=Decimal_to_binary(decimal)
print("Binary equivalent: ",bina)

"""python day17_p1.py
Enter a binary number: 10101
Decimal equivalent:  21
Enter a decimal number: 21
Binary equivalent:  10101"""