# Lambda function to add two numbers
add = lambda x, y: x + y

# Example usage
result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")  # Output: The sum of 5 and 3 is: 8


# Lambda function to square a number
square = lambda x: x ** 2

# Example usage
number = 4
result = square(number)
print(f"The square of {number} is: {result}")  # Output: The square of 4 is: 16



# Lambda function to check if a number is even
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"

# Example usage
number = 7
result = is_even(number)
print(f"The number {number} is: {result}")  # Output: The number 7 is: Odd
