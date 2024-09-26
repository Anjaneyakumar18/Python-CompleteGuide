
# Identity Operators in Python

# Define two variables
a = [1, 2, 3]
b = a  # b references the same list as a
c = [1, 2, 3]  # c is a new list with the same content

# Using 'is' operator
print("a is b:", a is b)  # Output: True (same object)
print("a is c:", a is c)  # Output: False (different objects)

# Using 'is not' operator
print("a is not b:", a is not b)  # Output: False
print("a is not c:", a is not c)  # Output: True
