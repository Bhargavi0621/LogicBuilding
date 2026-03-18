"""Program to Calculate the Area of a Circle and Triangle:
Write a program to calculate the area of a circle given its radius and a triangle given its base and height. For example:
Input: Radius: 5, Base: 10, Height: 4
Output:Area of Circle: 78.5
Area of Triangle: 20"""
import math
radius=float(input("Radius:"))
base=float(input("Base:"))
height=float(input("Height:"))
print("Area of Circle:", math.pi * radius ** 2)
print("Area of Triangle:", 0.5 * base * height)
"""python day3_p2.py
Radius: 4 
Base: 20
Height: 5
Area of Circle: 50.26548245743669
Area of Triangle: 50.0"""