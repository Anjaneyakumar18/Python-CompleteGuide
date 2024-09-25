def check_odd_even(num):
    """Checks if the number is odd or even."""
    if num % 2 == 0:
        return "Even"  # Number is even
    else:
        return "Odd"  # Number is odd

# Example usage
number = 10  # Change this number to test different inputs
result = check_odd_even(number)
print(f"The number {number} is {result}.")  # Output: The number 10 is Even.


def sum_two_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b  # Add the two numbers and return the result

# Example usage
num1 = 5  # First number
num2 = 3  # Second number
result = sum_two_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {result}.")  # Output: The sum of 5 and 3 is 8.


def display_arguments(*args):
    """Displays the arguments passed to the function."""
    print("Arguments received:")
    for arg in args:  # Iterate through each argument
        print(arg)  # Print each argument

# Example usage
display_arguments(1, "hello", 3.14, True)  # Can pass multiple types of arguments




def list_length(my_list):
    """Returns the length of the provided list."""
    return len(my_list)  # Use the built-in len() function to get the list length

# Example usage
sample_list = [1, 2, 3, "apple", "banana", True]  # A sample list with different types of elements
length = list_length(sample_list)  # Get the length of the list
print(f"The length of the list is: {length}.")  # Output: The length of the list is: 6.
