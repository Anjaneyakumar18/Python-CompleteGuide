class myexp(Exception):
    def __init__(self,message):
        super().__init__(self)
        self.message=message
    def error(self):
        print("User Error : 201")

n=int(input())
if n<0:
    try:
        raise myexp("No negitive numbers")
    except myexp as e:
        print(e.message)
        e.error()