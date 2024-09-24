# In previous file we have discussed Private access modifier 
# let's look into protected access modifier

''''
        parent
          ^
          |
          |
        child
child class is inherited from parent so
it can only use parent class protected resorces 
          
'''

class parent:
    def __init__(self,model,year):
        self._model=model
        self._year=year

    def _details(self):
        print('This is protected method form parent class')

class child(parent):
    def __init__(self,model,year,customer):
        super().__init__(model,year)
        self.customer=customer
    
    def access(self):
        print(f'Model : {self._model}\nYear : {self._year}')


mustang=child('Boss 429',"1969","AK18")
mustang.access()