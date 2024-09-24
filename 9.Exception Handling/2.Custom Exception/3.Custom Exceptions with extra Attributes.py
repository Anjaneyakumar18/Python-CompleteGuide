class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message=message
        self.status=400 #extra attribute in the Custom exception class
try:
    raise MyException("Custom exception with extra attribute")
except MyException as e:
    print(e.status)
    