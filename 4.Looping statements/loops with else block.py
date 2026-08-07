for i in range(10):
    print("first loop")
else:
    print("loop executed with out break so else executing or else else would have terminated")

for i in range(10):
    if i==9:
        break
    print(i)
else:
    print("loop body executed with a break so else block is skipped")




i:int=10
while i>=5:
    i-=1
else:
    print("WHile loop exit normally without  a break so do the else block execuing or else While loop would have skipped")


while i>=0:
    if i==3:
        break
    i-=1
else:
    print("while loop exit due to a break so else block is executed!!")



