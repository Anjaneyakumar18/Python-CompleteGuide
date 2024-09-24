d = {1: 'a', 2: 'b', 3: 'c'}

key = int(input("Enter Key: "))

try:
    print(f"The value for key {key} is: {d[key]}")
except KeyError as e:
    print(f"KeyError: The key {key} does not exist in the dictionary.")