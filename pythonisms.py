import pytest

""""
Feature Tasks and Requirements
Create examples demonstrating pythonic language features. 

***********iterator/generator
For example…
Use iterators/generators on a custom collection to…
add ability to be used in a for in loop
add ability to be used in a list comprehension
add ability to convert to a list or other collection type
"""

class MyCollection:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __iter__(self):
        for item in self.data:
            yield item




# Use it in a for loop
collection = MyCollection()
for i in collection:
    print(i)

# Use it in a list comprehension
squared = [x**2 for x in collection]
print(squared)

# Convert to a list
new_list = list(collection)
print(new_list)




"""
# ************decorator
Create a decorator that adds behavior to a given function. For example…
Calculate the time spent in the function
Log relevant info for debugging purposes
Slow down the function
Convert the return value in some way
Validate some condition on the way in
"""

import time
import functools

def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in: {end - start} secs")
        return result
    return wrapper

@time_decorator
def my_function():
    time.sleep(1)

my_function()

import pythonisms 


""""
# ************Dunder 
Use dunder methods make your code more readable and elegant. For example…
add ability for two custom data structure to be considered equal
add ability for custom data structure to be considered truthy/falsy
"""
class MyDataStructure:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __bool__(self):
        return bool(self.data)

my_data1 = MyDataStructure([1, 2, 3])
my_data2 = MyDataStructure([1, 2, 3])
my_data3 = MyDataStructure([])

# Check for equality
print(my_data1 == my_data2) # True
print(my_data1 == my_data3) # False

# Check for truthiness
print(bool(my_data1)) # True
print(bool(my_data3)) # False




