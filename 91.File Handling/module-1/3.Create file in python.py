#Create a file in python is very easy

# there is no special method to createfile in python 

#we can use Open() method with write permission to create a file

# we can use x(Exclusive file creation) permission as well to create new file if file exists throws error
#Syntax:---
'''
with open("file location as a string","permission") as instance:
    //statements

'''

#example

filepath="New file.txt"
permission="x"
with open(filepath,permission) as FILE:
    print(f"New file is created as {filepath}")
    FILE.close()


#we can even pass string arguments as well

with open("newFile.txt","x") as f:
    print("File created")


