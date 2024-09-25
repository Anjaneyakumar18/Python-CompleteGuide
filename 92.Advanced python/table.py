class Table:
    def __init__(self):
        print('Empty Table created')
        self.table=[]
    
    def addRow(self,id,name,age):
        self.table.append([id,name,age])

    def display_Table(self):
        print("Id     Name      Age")
        for lst in self.table:
            for detail in lst:
                print(detail,end=" ")
            print()

newtable=Table()
newtable.addRow(101010,"anil kumar",20)
newtable.addRow(202020,"Ajay kumar",20)
newtable.display_Table()



'''
out put::
Empty Table created
Id     Name      Age
101010 anil kumar 20
202020 Ajay kumar 20
'''