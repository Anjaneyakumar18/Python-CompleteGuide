class parent:

    def method(self):
        print('from parent class - before overriding')

class child(parent):

    def method(self):
        print("child class after overriding")

# object for Parent class

obj2=parent()
obj2.method()

# object for child class

obj=child()
obj.method()