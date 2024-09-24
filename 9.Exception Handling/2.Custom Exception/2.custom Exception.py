# Creating a Custom error
# If inputed password length is less than 6 raise a Password error

class passwordExp(Exception):
    def __init__(self,msg):
        super().__init__(msg)
password=input("Enter password :")

if len(password)<6:
    try:
        raise passwordExp("Invalid password")
    except passwordExp as e:
        print(e)
else:
    print("Valid Password")
        