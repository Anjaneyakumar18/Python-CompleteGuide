class Point:
    def __init__(self,a:int):
        self.a=a

    def __str__(self):
        return f"The object value is {self.a}"
    def __add__(self,other):
        return self.a+other.a

    def __sub__(self,other):
        return self.a-other.a

    def __mul__(self,other):
        return self.a*other.a

    def __floordiv__(self, other):
        return self.a // other.a

    def __mod__(self, other):
        return self.a%other.a

    def __gt__(self,other):
        return self.a>other.a

    def __lt__(self, other):
        return self.a<other.a

    def __ge__(self, other):
        return self.a>=other.a

    def __le__(self, other):
        return self.a<=other.a

    def __eq__(self, value):
        return self.a==value


p1=Point(10)
p2=Point(20)
print(p1,p2)
#print(p1+p2) -->> Returns an error due to un supported opartor as sum of 2 object is not possible but can be done using Opertaor iverloading

print(p1+p2)
print(p1-p2)
print(p1*p2)
print(p1//p2)
print(p1>p2)
print(p1<p2)
print(p1<=p2)
print(p1>=p2)
print(p1==10)