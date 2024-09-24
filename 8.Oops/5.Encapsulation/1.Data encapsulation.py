class Employee:
    def __init__(self,name,age,phoneno,email):
        self.name=name
        self.age=age
        # private data member - ph no
        self.__phonenumber=phoneno
        #private data members - email
        self.__email=email

    def view(self):
        print(f'Name : {self.name}\nAge : {self.age}')

    def phonenumber(self):
        print(f'Phone Number : {self.__phonenumber}')

    def email(self):
        print(f'Email : {self.__email}')

e1=Employee('ak',20,1234567,'ak@gmail.com')

print(e1.name)

print(e1.age)

# print(e1.__phonenumber)


#print(el.__email)
e1.view()
e1.email()
e1.phonenumber()