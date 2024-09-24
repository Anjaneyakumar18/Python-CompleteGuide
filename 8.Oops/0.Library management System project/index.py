# main.py
from admin import Admin
from librarian import Librarian
from user import User
from library import Library

# Create an admin instance
admin = Admin("AK", 20, 12345, "New York")

# Adding Books
print("\nAdding Books:")
admin.add_book(1, "Power of Subconscious Mind", "Joseph Murphy", 399, "ABC Store")
admin.add_book(2, "Atomic Habits", "James Clear", 299, "XYZ Store")
admin.add_book(3, "Clean Code", "Robert C. Martin", 599, "DEF Store")

# View Book
print("\nViewing Books:")
librarian = Librarian("Jane Doe", "Female", 30, 9876543210, "Los Angeles")
librarian.view_book(1)
librarian.view_book(2)
librarian.view_book(4)  # Book not in the list to check error handling

# Removing a Book
print("\nRemoving a Book:")
librarian.remove_book(2)
librarian.view_book(2)  # Verify if the book has been removed

# Hire and Fire Librarian
print("\nManaging Librarians:")
admin.hire_librarian("John Smith", "Male", 40, 1234567890, "Chicago")
admin.hire_librarian("Emily Brown", "Female", 28, 1122334455, "Boston")
print(f"Current librarians: {[librarian.Librarian_name for librarian in Library.Librarians]}")

admin.fire_librarian("John Smith")
print(f"Current librarians after firing: {[librarian.Librarian_name for librarian in Library.Librarians]}")

# Adding Users
print("\nAdding Users:")
user1 = User("Alice", 25, "Female", "123 Main St", "555-5555", "Regular")
user2 = User("Bob", 30, "Male", "456 Elm St", "555-1234", "Premium")
Library.Users.append(user1)
Library.Users.append(user2)
print(f"Current users: {[user.user_name for user in Library.Users]}")

# Allotting a Book to a User
print("\nAllotting Book to a User:")
librarian.allot_book("Alice", "Power of Subconscious Mind")

# Viewing Allotted Books for a User
print("\nAlice's Borrowed Books:")
for book in user1._books:
    print(f'Book Name: {book.book_name}, Author: {book.author}')

# Returning a Book
print("\nReturning a Book:")
librarian.return_book("Alice", "Power of Subconscious Mind", took_date=(2024, 9, 1), give_date=(2024, 9, 10))

# User Requests a Book
print("\nUser Requests a Book:")
user1.request_book("Atomic Habits")

# User Returns a Book
print("\nUser Returns a Book:")
user1.return_book("Atomic Habits")

# Updating User Information
print("\nUpdating User Information:")
user1.update_member()
