'''A generator is an object that produces values one at a time instead of creating all values at once.

Instead of storing every value in memory, it generates values only when needed.'''

def genarte(n):
    i=0
    while i<n:
        yield i   ''' Yield vs return is a famous question where retrun actually returns the method while a yield return and save where the execution has stoped'''
        i+=1
gen=genarte(5)
for i in range(4):
    print(next(gen))
