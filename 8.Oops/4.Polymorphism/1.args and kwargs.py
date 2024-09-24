def allEle(*args):
    for ele in args:
        print(ele,end=" ")
    print()

def everykey(**kwargs):
    for key in kwargs.keys():
        print(f'{key} - {kwargs[key]}')

allEle(1,2,3,4,5,6,7)

everykey(name="Ak",age=20,height='175cm')
