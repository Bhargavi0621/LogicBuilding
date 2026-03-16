"""Write a Program to Find the Size of int, float, double, and char on Your Computer:
Write a program that displays the size of fundamental data types (int, £1oat, double, and char) on your system. For example:
Output:
Size of int: 4 bytes
Size of float: 4 bytes
Size of double: 8 bytes
Size of char: 1 byte"""

import sys
print("Size of int: ", sys.getsizeof(int(21)), "bytes")  
print("Size of float: ", sys.getsizeof(float(3.45)), "bytes")   
print("Size of double: ", sys.getsizeof(float(21.6)), "bytes")
print("Size of char: ", sys.getsizeof(str('B')), "bytes")       