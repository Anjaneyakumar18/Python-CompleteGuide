
# Bitwise Operators in Python

# Define two variables
a = 10  # In binary: 1010
b = 4   # In binary: 0100

# Bitwise AND
bitwise_and = a & b
print("Bitwise AND (a & b):", bitwise_and)  # Output: 0

# Bitwise OR
bitwise_or = a | b
print("Bitwise OR (a | b):", bitwise_or)    # Output: 14

# Bitwise XOR
bitwise_xor = a ^ b
print("Bitwise XOR (a ^ b):", bitwise_xor)  # Output: 14

# Bitwise NOT
bitwise_not_a = ~a
bitwise_not_b = ~b
print("Bitwise NOT (~a):", bitwise_not_a)   # Output: -11 (in 2's complement)
print("Bitwise NOT (~b):", bitwise_not_b)   # Output: -5

# Left Shift
left_shift = a << 1
print("Left Shift (a << 1):", left_shift)   # Output: 20 (10100 in binary)

# Right Shift
right_shift = a >> 1
print("Right Shift (a >> 1):", right_shift) # Output: 5 (0101 in binary)
