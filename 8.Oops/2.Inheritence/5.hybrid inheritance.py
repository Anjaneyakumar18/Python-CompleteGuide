# Base class 'Employee' holds common attributes and methods for all employee types
class Employee:
    def __init__(self, name, age) -> None:
        self.Name = name
        self.age = age

    # Method to display the name and age of the employee
    def Emp(self):
        print(f"Name: {self.Name}, Age: {self.age}")

# 'frontend_devloper' class inherits from 'Employee' and adds specific attributes and methods related to frontend development
class frontend_devloper(Employee):
    def __init__(self, name='', age=0, fskills=None):
        # Initialize 'Employee' only if valid name and age are provided
        if name != '' and age != 0:
            super().__init__(name, age)
        if fskills is None:
            fskills = []
        self.fskills = fskills

    # Method to return frontend skills as a comma-separated string
    def frontend_dev(self):
        return f"{', '.join(self.fskills)}"

# 'backend_devloper' class inherits from 'Employee' and adds specific attributes and methods related to backend development
class backend_devloper(Employee):
    def __init__(self, name='', age=0, skills=None):
        # Initialize 'Employee' only if valid name and age are provided
        if name != '' and age != 0:
            super().__init__(name, age)
        if skills is None:
            skills = []
        self.bskills = skills

    # Method to return backend skills as a comma-separated string
    def backend_dev(self):
        return f"{', '.join(self.bskills)}"

# 'database_engineer' class inherits from 'Employee' and adds specific attributes and methods related to database management
class database_engineer(Employee):
    def __init__(self, name='', age=0, skills=None):
        # Initialize 'Employee' only if valid name and age are provided
        if name != '' and age != 0:
            super().__init__(name, age)
        if skills is None:
            skills = []
        self.dskills = skills

    # Method to return database skills as a comma-separated string
    def database_devloper(self):
        return f"{', '.join(self.dskills)}"

# 'fullstackDevloper' class demonstrates hybrid inheritance by inheriting from multiple classes ('frontend_devloper', 'backend_devloper', 'database_engineer')
class fullstackDevloper(frontend_devloper, backend_devloper, database_engineer):
    def __init__(self, name, age, fskills, bskills, dskills, otherskills):
        # Properly initialize the base class 'Employee' and other inherited classes
        Employee.__init__(self, name, age)
        frontend_devloper.__init__(self, name, age, fskills)
        backend_devloper.__init__(self, name, age, bskills)
        database_engineer.__init__(self, name, age, dskills)
        self.otherskills = otherskills

    # Method to display full stack developer details including all skills
    def fullstack(self):
        print(f"Name: {self.Name}, Age: {self.age}")
        print(f"Front end skills: {self.frontend_dev()}")
        print(f"Backend skills: {self.backend_dev()}")
        print(f"Database skills: {self.database_devloper()}")
        print(f"Other skills: {', '.join(self.otherskills)}")

if __name__ == "__main__":
    # Creating an instance of 'fullstackDevloper' class with various skills
    Ak = fullstackDevloper(
        "Anil Kumar", 20,
        ['html', 'css', 'js', 'bootstrap', 'jquery', 'Angular'],  # Frontend skills
        ['Nodejs', 'Expressjs'],                                 # Backend skills
        ['Sql', 'Mysql'],                                        # Database skills
        ['Git control version', 'DSA', 'Communication']          # Other skills
    )

    # Display the full stack developer's skills and information
    Ak.fullstack()
