
from datetime import date
from book import Book
from library import Library
from user import User

class Librarian:

    def __init__(self, Librarian_name, Librarian_gender, Librarian_age, Librarian_phno, Librarian_address):
        self.Librarian_name = Librarian_name
        self.Librarian_gender = Librarian_gender
        self.Librarian_age = Librarian_age
        self._Librarian_phno = Librarian_phno
        self._Librarian_address = Librarian_address

    def add_book(self, book_id, book_name, author, cost, store):
        try:
            new_book = Book(book_id, book_name, author, cost, store)
            Library.Books.append(new_book)
            print(f'Book "{book_name}" added successfully.')
        except Exception as e:
            print(f"Error adding book: {e}")
        return

    def remove_book(self, book_id):
        try:
            for book in Library.Books:
                if book.book_id == book_id:
                    Library.Books.remove(book)
                    print(f'Book "{book.book_name}" removed successfully.')
                    return
            print("Book not found.")
        except Exception as e:
            print(f"Error removing book: {e}")
        return

    def allot_book(self, customer, book_name):
        try:
            user_obj = None
            for user in Library.Users:
                if user.user_name == customer:
                    user_obj = user
                    break

            book_obj = None
            for book in Library.Books:
                if book.book_name == book_name:
                    book_obj = book
                    break

            if user_obj and book_obj:
                self.update_book(book_obj)
                user_obj.book_arr_update(book_obj)
                print(f'Book "{book_name}" allotted to {customer}.')
            else:
                print("User or Book not found.")
        except Exception as e:
            print(f"Error allotting book: {e}")
        return

    def return_book(self, customer, book, took_date, give_date):
        try:
            bill = self.calculate_bill(took_date, give_date)
            fine = self.calculate_fine(took_date, give_date)

            book_obj = None
            for bookobj in Library.Books:
                if bookobj.book_name == book:
                    book_obj = bookobj
                    break

            if book_obj:
                self.update_book(book_obj)
                print(f'Book "{book}" returned by {customer}. Bill: {bill}, Fine: {fine}')
                # Add more logic to update user's borrowed books
            else:
                print("Book not found.")
        except Exception as e:
            print(f"Error returning book: {e}")
        return

    def calculate_fine(self, took_date, give_date):
        try:
            # Convert took_date and give_date to date objects
            date1 = date(took_date[0], took_date[1], took_date[2])
            date2 = date(give_date[0], give_date[1], give_date[2])
            diff = (date2 - date1).days
            if diff > 30:
                return (diff - 30) * 2
            return 0  # No fine if the book is returned within 30 days
        except Exception as e:
            print(f"Error calculating fine: {e}")
            return 0

    def calculate_bill(self, took_date, give_date):
        try:
            # Convert took_date and give_date to date objects
            date1 = date(took_date[0], took_date[1], took_date[2])
            date2 = date(give_date[0], give_date[1], give_date[2])
            diff = (date2 - date1).days
            if diff > 0:
                return diff * 5  # Example billing rate: 5 units per day
            return 0
        except Exception as e:
            print(f"Error calculating bill: {e}")
            return 0

    def update_book(self, book):
        try:
            # Implement logic to update book status in the library
            print(f'Book "{book.book_name}" status updated.')
        except Exception as e:
            print(f"Error updating book: {e}")
        return

    def view_book(self, book_id):
        try:
            for book in Library.Books:
                if book.book_id == book_id:
                    print(f'Book ID: {book.book_id}, Name: {book.book_name}, Author: {book.author}, Cost: {book._cost}')
                    return
            print("Book not found")
        except Exception as e:
            print(f"Error viewing book: {e}")
        return
