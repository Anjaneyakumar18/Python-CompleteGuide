class Employee:
    
    def __init__(self,name,age,email,phomenumber):
        # intialising public data members into object
        self.name=name
        self.age=age
        
        # private data 
        self.__phonenumber=phomenumber
        self.__email=email

    def view(self):
        print(f'Name : {self.name}\nAge : {self.age}')

    def phonenumber(self):
        print(f'Phone Number : {self.__phonenumber}')

    def email(self):
        print(f'Email : {self.__email}')
    def updateEmail(self,email):
        self.__emailupadate(email)

    def updatePhone(self,ph):
        self.__phonenumberupdate(ph) 

#   encapsualated methods
    def __emailupadate(self,newmail):
        self.__email=newmail
        print('successfully updated')

    def __phonenumberupdate(self,newph):
        self.__phonenumber=newph
        print('successfully updated')



E1=Employee('AK',20,123456,'ak@gmail.com')

E1.view()

E1.phonenumber()
E1.email()

E1.updateEmail('ak18@gmail.com')
E1.updatePhone(864934)

E1.phonenumber()
E1.email()     