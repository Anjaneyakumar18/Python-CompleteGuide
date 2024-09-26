# if_else_demo.py

# Demonstrating if-else statements with different conditions

# Check if a number is positive, negative, or zero
number = 15

print(f"Checking the number: {number}")
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative or zero.")

print()  # Blank line for readability

# Check if a grade corresponds to a letter grade
grade = 82
print(f"Checking the grade: {grade}")

if grade >= 90:
    print("You got an A!")
else:
    if grade >= 80:
        print("You got a B!")
    else:
        if grade >= 70:
            print("You got a C!")
        else:
            if grade >= 60:
                print("You got a D!")
            else:
                print("You got an F!")

print()  # Blank line for readability

# Check if a character is a vowel or consonant
char = 'e'
print(f"Checking the character: '{char}'")

if char in 'aeiouAEIOU':
    print(f"'{char}' is a vowel.")
else:
    print(f"'{char}' is a consonant.")

print()  # Blank line for readability

# Check if a number is even or odd
number = 8
print(f"Checking if {number} is even or odd.")

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

print()  # Blank line for readability

# Check if a user is old enough to vote
age = 18
print(f"Checking if age {age} is eligible to vote.")

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
