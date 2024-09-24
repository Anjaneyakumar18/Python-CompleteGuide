# This code demonstrates multi-level inheritance in Python.
# The 'Parent' class inherits from 'grandparents' class, and the 'child' class inherits from 'Parent' class.

# Definition of the 'grandparents' class
class grandparents:
    # Constructor method to initialize the grandparents class with the name attribute
    def __init__(self, name):
        self.name = name

    # Method to describe the height of the grandparents
    def height(self):
        print("182 cm")

# The 'Parent' class inherits from the 'grandparents' class
class Parent(grandparents):
    # Constructor method to initialize the Parent class with name and gender attributes
    def __init__(self, name, gender):
        super().__init__(name)  # Calling the grandparents' constructor using super()
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
kid.eyes()    # Output: Gray eyes
kid.nose()    # Output: flat nose

# Calling the method specific to the child class
kid.assets()  # Output: House, Cars and Land

# Calling the method inherited from the grandparents class
kid.height()  # Output: 182 cm
