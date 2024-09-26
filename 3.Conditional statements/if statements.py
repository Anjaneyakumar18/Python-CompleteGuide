# if_block_demo.py

# Check numbers
numbers = [10, -5, 0, 4, 7]

for num in numbers:
    print(f"Checking the number: {num}")
    
    # Basic if-elif-else structure
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    # Nested if example
    if num != 0:
        if num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    
    print()  # Add a blank line for readability

# Check grades
grades = [95, 85, 72, 58]

for grade in grades:
    print(f"Checking the grade: {grade}")
    
    # Using if-elif-else for grading system
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

    print()  # Add a blank line for readability
