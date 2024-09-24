class myexception(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Input for age
Age = input("Enter Age: ")

try:
    Age = int(Age)  # Convert the input to an integer
except ValueError as e:
    print("Invalid input. Please enter a valid number.")  # Handle invalid input
    exit()  # Exit if input is not a valid integer

# Check if age is negative
if Age < 0:
    try:
        raise myexception("Age cannot be negative")  # Raise an exception if age is negative
    except myexception as e:
        print(e)
else:
    print(f"Your age is {Age}.")