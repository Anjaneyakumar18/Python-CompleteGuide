# This code demonstrates multiple inheritance in Python.
# The 'child' class inherits from both 'Parent' and 'uncle' classes.

# Definition of the 'uncle' class
class uncle:
    # Constructor method to initialize the uncle class with the name attribute
    def __init__(self, name):
        self.name = name

    # Method to describe the height of the uncle
    def height(self):
        print("182 cm")

# Definition of the 'Parent' class
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

# The 'child' class inherits from both 'Parent' and 'uncle' classes
class child(Parent, uncle):
    # Constructor method to initialize the child class with name and gender attributes
    def __init__(self, name, gender):
        # Calling the Parent's constructor
        Parent.__init__(self, name, gender)
        # Calling the uncle's constructor
        uncle.__init__(self, name)

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

# Calling the method inherited from the uncle class
kid.height()  # Output: 182 cm
