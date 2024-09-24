## In java Acccess modifiers  are
'''
    1.Public
    2.protected
    3.Private
    4.default

'''

#Public Access Modifier:

'''Least abstraction: Members (attributes and methods) defined as public
 are accessible from any part of the program. There is no restriction 
 on their visibility.'''


#Private Access Modifier:

'''Highest abstraction: Members defined as private are only accessible
 within the class they are declared in. They cannot be accessed or modified
directly from outside the class, providing the highest level of 
encapsulation and data hiding.'''


#Protected Access Modifier:

'''Intermediate level of abstraction: Members defined as protected are 
accessible within the class they are declared in and also in subclasses 
(derived classes). They are not accessible from outside these classes, 
providing a middle ground between public and private access.
'''


# In python
""" 
   1. Public ---> variable name or method name eg: age,display()

   2. protected ---> _variablename or _methodname   one underscore is used 

   3. private ---> __variablename or __method name   two under scores are used

 """

# we cannot access private data members and member functions out side the class wich throws errors

class AccessModifiers_demo:
    def __init__(self,name,age,phno):
        self.name=name
        self.age=age
        self.__phone_num=phno

    def dispaly(self):
        print(f'Name: {self.name}\nage: {self.age}\nHabit: {self.__phone_num}')

    def __call(self):
        print(f"called {self.__phone_num}")
    
    def makecall(self):
        print("About to make call")
        self.__call()

am=AccessModifiers_demo("ak",20,987654321)
am.dispaly()

print(am.name) # no error as name is public attribute

#print(am.__phone_num) #throws error as we are trying access private attribute out side class

am.makecall()  #public method accessing

am.__call()  # private method accessing thorws error

