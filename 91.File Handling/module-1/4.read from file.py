# In python we have open() method so we can open a file 
# after file opened we have a object for the file isn't it!!
# so we can access read() method using file object


#0.Example file.txt
'''
Heyy!! I am Anjaneya Kumar Ramisetty 
we are learning python file handling
this is example file
'''
with open("0.Example file.txt","r") as file:
    file_content=file.read()

    print(file_content)
    file.close()

#output:
'''
Heyy!! I am Anjaneya Kumar Ramisetty 
we are learning python file handling
this is example file
'''