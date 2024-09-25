# For the better understanding of this concepts first look into modules foldwr first

#math modules is most famous module in python here is how you use methods in math module


'''math.sqrt(x): Returns the square root of x.
math.pow(x, y): Returns x raised to the power of y.
math.ceil(x): Returns the smallest integer greater than or equal to x.
math.floor(x): Returns the largest integer less than or equal to x.
math.factorial(x): Returns the factorial of x.
math.gcd(x, y): Returns the greatest common divisor of x and y.
math.log(x, base): Returns the logarithm of x to the specified base (default is e).
math.sin(x): Returns the sine of x (in radians).
math.cos(x): Returns the cosine of x (in radians).
math.pi: Returns the value of Pi (π = 3.14159...).'''

# program 


import math

# 1. math.sqrt(x) - Square root of x
num = 16
print(f"Square root of {num}: {math.sqrt(num)}")

# 2. math.pow(x, y) - x raised to the power y
base = 2
exponent = 3
print(f"{base} raised to the power of {exponent}: {math.pow(base, exponent)}")

# 3. math.ceil(x) - Ceiling value of x
value = 4.3
print(f"Ceiling of {value}: {math.ceil(value)}")

# 4. math.floor(x) - Floor value of x
print(f"Floor of {value}: {math.floor(value)}")

# 5. math.factorial(x) - Factorial of x
n = 5
print(f"Factorial of {n}: {math.factorial(n)}")

# 6. math.gcd(x, y) - Greatest common divisor of x and y
a = 48
b = 18
print(f"GCD of {a} and {b}: {math.gcd(a, b)}")

# 7. math.log(x, base) - Logarithm of x to the given base
x = 100
base = 10
print(f"Logarithm of {x} with base {base}: {math.log(x, base)}")

# 8. math.sin(x) - Sine of x (in radians)
angle_rad = math.pi / 2  # 90 degrees in radians
print(f"Sine of 90 degrees: {math.sin(angle_rad)}")

# 9. math.cos(x) - Cosine of x (in radians)
print(f"Cosine of 90 degrees: {math.cos(angle_rad)}")

# 10. math.pi - Value of Pi
print(f"Value of Pi: {math.pi}")

