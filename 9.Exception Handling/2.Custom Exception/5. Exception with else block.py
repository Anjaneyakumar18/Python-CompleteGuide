class customException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)

try:
    name=input()
    if name=="Admin":
        raise customException("Name cannot be Admin")
except Exception as e:
    print(e)

else:
    print("Name opted successfully !!!!!")

