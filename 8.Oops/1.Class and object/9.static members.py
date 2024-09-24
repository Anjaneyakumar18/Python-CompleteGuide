'''
    In java static members are declared using satctic keyword but in python,
    static class datamembers are just declared out side of constructor or methods
'''

# static data members are accessed using class name


class static_demo:
    objects=0
    def __init__(self):
        static_demo.objects+=1



obj1=static_demo()
obj2=static_demo()
obj2=static_demo()


print(static_demo.objects)
