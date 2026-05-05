"""Dictionary Keys and Values
Task: Extract and print all the keys and values of a dictionary as separate lists.
Input:
data = {"name": "John", "age": 25, "city": "New York"}
Expected Output:
Keys: ["name", "age", "city"], Values: ["John", 25, "New York"]
"""

import json
data=json.loads(input("Enter the keys and values of a dictionary: "))
key=list(data.keys())
value=list(data.values())
print("Keys:",key)
print("Values: ",value)

"""python day30_p1.py
Enter the keys and values of a dictionary: {"name":"Bhargavi","age":26,"city":"manipal"}
Keys: ['name', 'age', 'city']
Values:  ['Bhargavi', 26, 'manipal']"""