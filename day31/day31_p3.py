"""3. Fibonacci Sequence
Task: Create a recursive function fibonacci(n) that returns the number in the Fibonacci sequence. Then, use a loop to print the sequence up to the term.
Input: n = 5
Expected Output: 0, 1, 1, 2, 3
"""

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter the number of terms: "))
for i in range(n):
    print(fibonacci(i), end=", ")

"""python day31_p3.py
Enter the number of terms: 8
0, 1, 1, 2, 3, 5, 8, 13, """