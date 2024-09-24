# book.py
class Book:

    def __init__(self, book_id, book_name, author, cost, store):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self._cost = cost
        self._store = store

    def book_extra_details(self):
        try:
            print(f'Cost: {self._cost}')
            print(f'Store: {self._store}')
        except Exception as e:
            print(f"Error displaying extra details: {e}")
