

# when you call base() the controll comes here
def decorator(func):
    # Internal function that adds extra functionality
    def extra_functionality():
        print("Before calling the base function")
        func()  # Base function called
        print("After calling the base function")
    return extra_functionality  # Returning extra functionality method

# Declaring that base() is the function which is going to get extra functionality using @decorator
@decorator
def base():
    print("This is the base function")

# Calling the base method, which has added extra functionalities
base()
