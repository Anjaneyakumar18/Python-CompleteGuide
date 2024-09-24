#method 1
length=int(input("Enter length of list"))
lst=[]
for i in range(length):
    lst.append(int(input("Enter element")))
print(lst)
#method2
lst=list(map(int,input("Enter all list elements with space saparations").split()))
print(lst)