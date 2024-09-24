# This code demonstrates simple inheritance in Python.
# The 'Parent' class defines attributes and methods that are inherited by the 'child' class.

class Parent:
    # Constructor method to initialize the Parent class with name and gender attributes
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    # Method to describe the eye color of the Parent
    def eyes(self):
        print("Gray eyes")

    # Method to describe the nose type of the Parent
    def nose(self):
        print("flat nose")

# The 'child' class inherits from the 'Parent' class
class child(Parent):
    # Constructor method to initialize the child class with name and gender attributes
    def __init__(self, name, gender):
        super().__init__(name, gender)  # Calling the Parent's constructor using super()

    # Method specific to the child class
    def assets(self):
        print("House, Cars and Land")

# Creating instances of the Parent class
dad = Parent("mike", "M")
mom = Parent("ruth", "F")

# Creating an instance of the child class
kid = child("jenna", "F")

# Calling methods inherited from the Parent class
kid.eyes()  # Output: Gray eyes
kid.nose()  # Output: flat nose

# Calling the method specific to the child class
kid.assets()  # Output: House, Cars and Land
