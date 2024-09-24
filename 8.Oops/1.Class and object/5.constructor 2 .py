class student:
    def __init__(self,name,branch,section):

        self.name=name        # registering name,branch,section 
        self.branch=branch    # into the object 
        self.section=section

    def display(self):
        print("\nName :",self.name,"\nBranch :",self.branch,"\nSection:",self.section)

Ak=student("AK45","CSE","A")

Ak.display()

Nt=student("NtI0","CSE","C")

Nt.display()
