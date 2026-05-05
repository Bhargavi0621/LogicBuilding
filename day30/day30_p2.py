"""Merge Two Dictionaries
Task: Combine the items of two dictionaries into a single new dictionary.
Input:
dict1 = {"name": "John", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
Expected Output:
{'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}
"""

import json
dict1=json.loads(input("Enter the keys and values of a dictionary 1: "))
dict2=json.loads(input("Enter the keys and values of a dictionary 2: "))
dict1.update(dict2)
print(dict1)

"""python day30_p2.py
Enter the keys and values of a dictionary 1: {"name": "Bhargavi", "age": 26}       
Enter the keys and values of a dictionary 2: {"city": "Manipal", "country": "India"} 
{'name': 'Bhargavi', 'age': 26, 'city': 'Manipal', 'country': 'India'}"""