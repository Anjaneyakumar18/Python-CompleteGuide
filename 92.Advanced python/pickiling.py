import pickle as pk

my_dict = {1: 2, 3: 4, 5: 6}

with open("ex.txt", "wb") as file:
    pk.dump(my_dict, file)
with open("ex.txt",'rb') as file:
    print(pk.load(file))