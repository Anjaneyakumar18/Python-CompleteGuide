lst=[1,2,3,4,5,6,7,8,9,10]
left=0
right=len(lst)-1
while right>=left:
    temp=lst[right]
    lst[right]=lst[left]
    lst[left]=temp
    right-=1
    left+=1
print(lst)