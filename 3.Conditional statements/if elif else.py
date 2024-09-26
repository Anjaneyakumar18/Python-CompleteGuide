# if_elif_else_demo.py

# Check if a number is positive, negative, or zero
number = -5
print(f"Checking the number: {number}")

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print()  # Blank line for readability

# Check grade and assign a letter grade
grade = 87
print(f"Checking the grade: {grade}")

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")
else:
    print("You got an F!")

print()  # Blank line for readability

# Check if a character is a vowel or consonant
char = 'o'
print(f"Checking the character: '{char}'")

if char in 'aeiouAEIOU':
    print(f"'{char}' is a vowel.")
elif char.isalpha():
    print(f"'{char}' is a consonant.")
else:
    print("Not a valid alphabet character.")

print()  # Blank line for readability

# Check if a number is even, odd, or zero
number = 0
print(f"Checking if {number} is even, odd, or zero.")

if number == 0:
    print("The number is zero.")
elif number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

print()  # Blank line for readability

# Check if a user is eligible for a senior discount
age = 65
print(f"Checking if age {age} is eligible for a senior discount.")

if age >= 65:
    print("You are eligible for a senior discount.")
elif age >= 18:
    print("You are not a senior, but you are an adult.")
else:
    print("You are a minor.")
