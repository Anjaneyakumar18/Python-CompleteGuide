# include abc class and abstractmethod from Abstract base class

from abc import ABC, abstractmethod

class shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class rectangle(shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width


    def area(self):
        print(f'Area is {self.width*self.height}')

    def perimeter(self):
        print(f'Perimeter is {2*(self.width+self.width)}')
    
class Circle(shape):

    def __init__(self,radius):
        self.radius=radius

    def area(self):
        area=3.146*(self.radius**2)

        print(f'Area is {area}')

    def perimeter(self):
        p=2*3.146*self.radius

        print(f'Perimeter is {p}')
    

# Instantiate main2 and call method1
rect=rectangle(5,5)
C=Circle(10)
rect.area()
rect.perimeter()
C.area()
C.perimeter()

