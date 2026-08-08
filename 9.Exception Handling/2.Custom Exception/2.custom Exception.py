# Creating a Custom error
# If inputed password length is less than 6 raise a Password error

class passwordExp(Exception):
    def __init__(self,msg):
        super().__init__(msg)
password=input("Enter password :")

try:
    if len(password)<6:
        raise passwordExp("Password cannot be less the 6 chars")
    print(f'your password is {password}')
except Exception as e:
    print(e)
