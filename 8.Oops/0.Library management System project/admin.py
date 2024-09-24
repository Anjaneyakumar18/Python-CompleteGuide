# admin.py
from librarian import Librarian

class Admin(Librarian):

    def __init__(self, name, age, phone_no, address):
        self.name = name
        self.age = age
        self.__phone_num = phone_no
        self.__address = address

    def hire_librarian(self, Librarian_name, Librarian_gender, Librarian_age, Librarian_phno, Librarian_address):
        try:
            new_librarian = Librarian(Librarian_name, Librarian_gender, Librarian_age, Librarian_phno, Librarian_address)
            from library import Library
            Library.Librarians.append(new_librarian)
            print(f'Librarian "{Librarian_name}" hired successfully.')
        except Exception as e:
            print(f"Error hiring librarian: {e}")

    def fire_librarian(self, Librarian_name):
        try:
            from library import Library
            for librarian in Library.Librarians:
                if librarian.Librarian_name == Librarian_name:
                    Library.Librarians.remove(librarian)
                    print(f'Librarian "{Librarian_name}" fired successfully.')
                    return
            print("Librarian not found.")
        except Exception as e:
            print(f"Error firing librarian: {e}")
