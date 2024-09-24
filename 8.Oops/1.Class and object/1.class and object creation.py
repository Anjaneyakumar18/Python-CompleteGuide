# my class declartion 
class myclass:
    # method in class 
    def mymethod(self):
        print("my method from my class")

#my class2 declartion
class myclass2:
    #mymethod in myclass2 
    def mymethod(self):
        print("my method from myclass2")

    def mymethod2(self):
        print("my method2 from myclass2")

myobj=myclass()

myobj.mymethod()

myobj2=myclass2()

myobj2.mymethod()

myobj.mymethod2()  # throws error as mymethod2 is method belongs to myclass2 