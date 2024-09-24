f=open("0.Example file.txt",'w')

read_permission=f.readable()
write_permission=f.writable()

print(f"Can we read file: {read_permission}\nCan we write into file: {write_permission}")