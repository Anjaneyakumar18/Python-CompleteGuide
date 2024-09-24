class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Object is created')

    def cleanup(self):
        print('Object is manually cleaned up!')

    def view(self):
        print(f'Name : {self.name}\nAge : {self.age}')

    def delete(self):
        del self

# Create an instance of myclass
obj = myclass("Ak", 20)

# View the object properties
obj.view()

# Manually call cleanup
obj.cleanup()

obj.delete()
obj.view()

# Attempting to call cleanup after deletion will raise an error
try:
    obj.cleanup()
except NameError as e:
    print(f'Error: {e}')
