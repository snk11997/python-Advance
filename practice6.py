a="hello"


print(a[0],a[1],a[2])
print(a[:])
print(a[-5:-2])

print(a[::-1])


b = a[::-1]
print(b)

import hashlib

# Hashing a string using SHA-256
my_string = "hello"
hashed_value = hashlib.sha256(my_string.encode()).hexdigest()
print(f"SHA-256 hash of '{my_string}': {hashed_value}")

class MyObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        # Define a custom hash function
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, MyObject) and self.value == other.value

obj1 = MyObject(10)
obj2 = MyObject(10)

# Using custom objects as dictionary keys
my_dict = {obj1: "value1"}
print(my_dict[obj2])  # Accesses the value using a different object with the same hashed value
