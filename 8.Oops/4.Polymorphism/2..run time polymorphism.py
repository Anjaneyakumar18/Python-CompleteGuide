#method overloding is not possible in Python but we can do something like this

class Operations:

    def add(self,*numbers):
        s=0
        for number in numbers:
            s+=number
        return s
    
    def multiply(self,*numbers):
        m=1
        for number in numbers:
            m*=number
        return m
    
O=Operations()
added=O.add(2,3,4)

mul=O.multiply(2,3,4)

print(f'Sum : {added} | Product : {mul}')