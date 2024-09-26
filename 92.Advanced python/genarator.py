def genarte(n):
    i=0
    while i<n:
        yield i
        i+=1
gen=genarte(5)
for i in range(4):
    print(next(gen))