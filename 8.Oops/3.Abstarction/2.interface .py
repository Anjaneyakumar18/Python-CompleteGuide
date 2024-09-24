# An ABC class with 0 method implementation is a interface in python

#including ABC and @abstaractmethod 

from abc import ABC , abstractmethod

class Interface(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2():
        pass

class implementations(Interface):
    ## all methods can be overridden and can be 
    # implemented here
    def method1(self):
        print("method1 implemented")
    
    def method2(self):
        print("method2 implemented")


obj=implementations()
obj.method1()