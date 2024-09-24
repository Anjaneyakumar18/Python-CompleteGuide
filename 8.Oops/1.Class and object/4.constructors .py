# A constructor is a special method which is invoked when ever the 
# object is created 

class Myclass:
    def __init__(self):
        print("Construntor invoked here")
        

obj=Myclass()    


''' out put :Construntor invoked here

   without calling __init__

'''

class myclass2:
    def __init__():
        print("As this is constructor with out self argument hence can be called using class name ")


myclass2.__init__()


'''
output:::As this is constructor with out self argument hence can be called using class name  
'''