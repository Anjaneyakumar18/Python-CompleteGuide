class main:
    classattribute='main class atrribute'

    def __init__(self):
        print("I am Constructor in main class")
        self.instanceattribute="Attribute of instance"


class child(main):
    classattribute="child class attribute"

    def __init__(self):
        print("I am Constructor in Child class")

    def test(self):
        print(__class__.classattribute)
        super().__init__()
        print(super().classattribute)
        print(self.instanceattribute)

obj=child()
obj.test()


#output  
'''
I am Constructor in Child class
child class attribute
I am Constructor in main class
main class atrribute
Attribute of instance
'''