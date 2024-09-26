'''from functools import reduce
def reduce_function(x,y):
    return x+y
lst=[1,2,3,4,5,6,7,8,9,10]
ans=reduce(reduce_function,lst)
print(ans)'''
d={}
for i in range(256):
    d[i]=chr(i)
print(d)