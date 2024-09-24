'''
  self:Current calling instance
'''

# self keyword in python is very much similar 
# to this keyword in java and javascript

class self_demo:
    def __init__(self):
        print('constructor')
    def fun(self):
        print("method in self_demo class")
    
    def fun2():
        print("fun2() from self_demo class")


sd=self_demo()

sd.fun()  ## calling fun() from self_demo class 

self_demo.fun2()  ## calling fun2() from self_demo using class name as it doesn't 
                  # has first argument as self  
                  # static method -- look into static.py file 
    

'''
        A method has no self attribute but accessed using self keyword 
        throws an error called positional arguments error   
    '''
'''
        A method has self attribute but accessed using without keyword 
        throws an error called positional arguments error   
    '''