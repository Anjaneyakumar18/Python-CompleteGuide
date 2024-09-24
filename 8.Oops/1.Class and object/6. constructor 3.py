class class1:
    def __init__():  # constructor of class
        print("From class1 constructor")

class class2:
    def __init__(self):
        print("class2 constructor") 
        class1.__init__()  #calling class1 constructor in class2 constructor 

myobj=class2()

