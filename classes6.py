# 1) Create a parent class:
#    a) Make a class with a constructor to store a name and an id.
#    b) Add a `display()` method to print the stored details.

# 2) Create a child class that inherits from the parent:
#    a) Add extra properties like salary and job role in its constructor.
#    b) Call the parent constructor inside the child constructor to set name and id.

# 3) Create an object of the child class:
#    a) Pass values for name, id, salary, and role.

# 4) Call the parent class method using the child object:
#    a) Use the object to call `display()` and print the details.

"""
Write a program to create a parent class Person (attributes - name, idnumber) 
with a method display to display the attributes. Create a child class Employee (attributes - name, idnumber, salary,
 post). 
Access the attributes of parent class in child class. Then, create an object for child class and call the display 
method 
to display the name and idnumber.
"""

class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(f"My name is {self.name} and my id number is {self.id}.")
class Employee(Person):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,id)
k = Employee("Nandan",8256,10,"Intern")
k.display()