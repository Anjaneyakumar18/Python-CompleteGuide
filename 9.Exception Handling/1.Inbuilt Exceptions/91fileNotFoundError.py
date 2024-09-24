fname=input("file name")
try:
    with open(fname) as file:
        matter=file.read()
        print(matter)
except FileNotFoundError as e:
    print(e)