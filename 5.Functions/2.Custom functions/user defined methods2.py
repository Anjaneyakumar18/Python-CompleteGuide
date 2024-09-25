def is_prime(num):
    """Checks if num is prime."""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Example usage
print(is_prime(7))  # Output: True



def reverse_string(s):
    """Returns the reversed string."""
    return s[::-1]

# Example usage
print(reverse_string("Hello"))  # Output: olleH

def find_max(numbers):
    """Returns the maximum number in the list."""
    max_num = numbers[0]  # Start with the first number
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example usage
print(find_max([3, 5, 7, 2]))  # Output: 7



def factorial(n):
    """Returns the factorial of n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120

