lst=[1,2,3,4,5,4,3,5,4,3,5,5]
hash_table={}
for ele in lst:
    if ele in hash_table:
        hash_table[ele]+=1
    else:
        hash_table[ele]=1
print(hash_table)
high=0
high_c=0
for num in hash_table.keys():
    if hash_table[num]>high_c:
        high=num
print(f"most repeating number is {high}")
