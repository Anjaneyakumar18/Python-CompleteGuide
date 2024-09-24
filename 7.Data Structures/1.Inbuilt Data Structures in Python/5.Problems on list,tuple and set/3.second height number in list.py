lst=[1,2,3,4,3,2,4,5,6,4,5,6]
#method 1
lst=sorted(list(set(lst)))
print(lst[-2])

#method 2

lst=[1,2,3,4,3,2,4,5,6,4,5,6]
first=lst[0]
second=lst[0]
for num in lst:
    if num>first:
        second=first
        first=num
print(f"second largest number is {second}")