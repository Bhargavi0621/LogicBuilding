"""Check if an Integer Can Be Expressed as the Sum of Two Prime Numbers:
Write a program to check if a number can be expressed as the sum of two prime numbers. Print all such combinations. 
For example:
Input: Enter a number: 34
Output:
34 = 3 + 31
34 = 5 + 29
34 = 11 + 23
34 = 17 + 17
"""

def is_prime(number):
    prime=True
    for i in range(2,int(number/2)+1):
        if number%i==0:
            prime=False
            break
    if prime:
        return True
    else:
        return False
    
number=int(input("Enter the number: "))
for i in range(2,int(number/2)+1):
    j=number-i
    if is_prime(i) and is_prime(j):
        print(f"{number}={i}+{j}")

"""python day16_p2.py
Enter the number: 48 
48=5+43
48=7+41
48=11+37
48=17+31
48=19+29"""