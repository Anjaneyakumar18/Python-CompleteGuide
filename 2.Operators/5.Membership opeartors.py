# Membership Operators in Python

# Define a list and a string
my_list = [1, 2, 3, 4, 5]
my_string = "Hello, World!"

# Using 'in' operator
check_list = 3 in my_list
check_string = 'Hello' in my_string

print("Is 3 in my_list?", check_list)              # Output: True
print("Is 'Hello' in my_string?", check_string)    # Output: True

# Using 'not in' operator
check_list_not = 6 not in my_list
check_string_not = 'Python' not in my_string

print("Is 6 not in my_list?", check_list_not)      # Output: True
print("Is 'Python' not in my_string?", check_string_not)  # Output: True

