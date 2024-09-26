def evens(num):
    return num%2==0

lst=[1,2,3,4,5,6]

lst2=filter(evens,lst)
print(list(lst2))


arr=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2!=0,arr)))

