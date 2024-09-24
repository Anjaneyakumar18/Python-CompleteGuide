from abc import ABC , abstractmethod

class main(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

    def method3(self):
        print("ABC - Method3")

class subclass(main):
    def method1(self):
        print("sub class - method1")

    def method2(self):
        print("subclass - method2")

    def method3(self):
        return super().method3()
    

obj1=main()
obj2=subclass()
obj2.method1()
obj2.method3()