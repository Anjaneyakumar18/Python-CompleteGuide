#we use with keyword in manage files 

#with keyword in python is used to mange resources (files,database etc..)

#in python we have a method called open() to open a file open has 2 arugemts 
#1:file path 2:permissions

# in file handling we have to create an object for the file which represents the 
#file as shown use as keyword for that
'''
with open(filepath,permission) as instance:
    //statements
    
'''

with open("newfile.txt","w") as file:
    '''
    operations here
    '''


# we can also directly open as below

f=open("0.Example file.txt")
