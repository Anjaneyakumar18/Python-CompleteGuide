with open('0.Example file.txt',"rb") as file:
    c=file.read()
    print(c)
    binary=("".join(format(byte,'b') for byte in c))
    print(binary)