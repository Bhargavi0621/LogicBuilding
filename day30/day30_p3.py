"""Task: Create a new dictionary where the original keys become values and the original values become keys (Dictionary Comprehension).
Input:
data = {"name": "John", "age": 25, "city": "New York"}
Expected Output:
{'John': 'name', 25: 'age', 'New York': 'city'}
"""
import json
dicti=json.loads(input("Enter the keys and values of a dictionary: "))
newdict = {value: key for key, value in dicti.items()}
print(newdict)

"""python day30_p3.py
Enter the keys and values of a dictionary: {"name":"Bhargavi","age":26,"city":"manipal"}
{'Bhargavi': 'name', 26: 'age', 'manipal': 'city'}"""