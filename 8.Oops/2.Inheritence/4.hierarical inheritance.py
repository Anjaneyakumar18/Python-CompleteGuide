# Hierarchical inheritance occurs when multiple derived classes inherit from a single base class.
# In this example, 'person' is the base class, and 'Employee' and 'Customer' could be derived classes.

# The 'person' class holds basic personal information
class person:
    # Constructor to initialize name, age, and gender
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to print personal information
    def person_info(self):
        print(f'Name: {self.name}\nAge: {self.age}\nGender: {self.gender}')

# The 'personal_info' class holds contact information
class personal_info:
    # Constructor to initialize private phone number and email attributes
    def __init__(self, phonenumber, email):
        self.__phonenumber = phonenumber
        self.__email = email

    # Method to print contact information
    def contact(self):
        print('Phone number:', self.__phonenumber)
        print('Email:', self.__email)

# The 'Employee' class inherits from both 'person' and 'personal_info', demonstrating multiple inheritance.
class Employee(person, personal_info):
    # Constructor to initialize attributes from both parent classes and its own attribute 'role'
    def __init__(self, name, age, gender, phno, email, role):
        person.__init__(self, name, age, gender)        # Initializing 'person' attributes
        personal_info.__init__(self, phno, email)       # Initializing 'personal_info' attributes
        self.role = role                                # Adding an attribute specific to 'Employee'

    # Method to display all information of the employee, including inherited and specific attributes
    def emp(self):
        self.person_info()  # Display personal information from 'person' class
        self.contact()      # Display contact information from 'personal_info' class
        print(f'Role: {self.role}')  # Display the role specific to 'Employee'

# Creating an instance of the Employee class
Ak = Employee('Anil Kumar', 20, 'Male', 55687, "ak@gmail.com", "SDE-I")

# Calling the method to display the employee's information
Ak.emp()
