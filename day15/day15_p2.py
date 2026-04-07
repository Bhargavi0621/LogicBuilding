"""Print Prime Numbers Within a Range:
Write a program to display all prime numbers between two intervals entered by the user. 
For example:
Input: Enter two numbers: 10, 30
Output: Prime numbers between 10 and 30: 11, 13, 17, 19, 23, 29"""

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
result=[]
for i in range(num1,num2):
    prime = True
    for j in range(2,int(i/2)+1):
        if i%j==0:
            prime=False
            break
    if prime:
        result.append(str(i))
print(f"Prime numbers between {num1} and {num2}: "+",".join(result))

"""python day15_p2.py
Enter the first number: 10
Enter the second number: 50
Prime numbers between 10 and 50: 11,13,17,19,23,29,31,37,41,43,47"""