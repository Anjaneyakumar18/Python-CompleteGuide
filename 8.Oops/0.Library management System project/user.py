# user.py
class User:

    def __init__(self, user_name, user_age, user_gender, user_address, user_phoneno, user_type):
        self.user_name = user_name
        self.user_age = user_age
        self.user_gender = user_gender
        self._user_address = user_address
        self._user_phoneno = user_phoneno
        self._user_type = user_type
        self._books = []

    def request_book(self, book):
        try:
            # Implement logic to request a book
            print(f'{self.user_name} requested the book "{book}".')
        except Exception as e:
            print(f"Error requesting book: {e}")

    def return_book(self, book):
        try:
            # Implement logic to return a book
            print(f'{self.user_name} returned the book "{book}".')
        except Exception as e:
            print(f"Error returning book: {e}")

    def update_member(self):
        try:
            # Implement logic to update member information
            print(f'User "{self.user_name}" information updated.')
        except Exception as e:
            print(f"Error updating member: {e}")

    def book_arr_update(self, book_obj):
        try:
            self._books.append(book_obj)
            print(f'Book "{book_obj.book_name}" added to {self.user_name}\'s borrowed list.')
        except Exception as e:
            print(f"Error updating borrowed books: {e}")
