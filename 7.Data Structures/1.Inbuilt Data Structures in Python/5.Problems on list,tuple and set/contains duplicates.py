#method1

lst=[1,2,3,4,5,6,7,7,2,3]
if len(lst)==len(set(lst)):
    print("List doesnt contains any dupliactes")
else:
    print("List has dupliacates")


#method2

hash_set=set()
lst=[1,2,3,4,5,6,3,4]
dup=True
for num in lst:
    if num not in hash_set:
        hash_set.add(num)
    else:
        print("Contains duplicates")
        dup=False
if dup:
    print("NO duplicates")

