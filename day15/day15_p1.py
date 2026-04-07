"""Check Whether a Number is Prime or Not:
Write a program that checks if a number entered by the user is a prime number.
For example:
Input: Enter a number: 17
Output: 17 is a prime number."""

number=int(input("Enter a number: "))
prime=True
if number<2:
    print(number,"is not a prime number.")
else:
    for i in range(2,int(number/2)+1):
        if number%i==0:
            prime=False
            break
    if prime:
        print(number,"is a prime number.")
    else:
        print(number,"is not a prime number.")

"""python day15_p1.py
Enter a number: 37
37 is a prime number."""