lst=list(map(int,input().split()))
index=int(input("Enter index"))
try:
    ele=lst[index]
    print(ele)
except IndexError as e:
    print(e)