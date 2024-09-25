# List of tuples (name, age)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Lambda function to sort by age
sorted_people = sorted(people, key=lambda x: x[1])

# Example usage
print(f"People sorted by age: {sorted_people}")  # Output: People sorted by age: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
