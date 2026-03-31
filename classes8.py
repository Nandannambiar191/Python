# Q) Write a Python program to show inheritance using Person and Student classes.

# Follow the steps below:

# 1. Create a parent class named Person.

# 2. Inside the Person class, create a constructor using __init__().
#    - It should take two values:
#      fname → first name
#      lname → last name

# 3. Store these values inside the object using:
#    self.firstname
#    self.lastname

# 4. Create a method named printname().
#    - This method should print the full name of the person.

# 5. Create a child class named Student that inherits from Person.

# 6. Inside the Student class, create a constructor using __init__().
#    - It should take:
#      fname
#      lname
#      year

# 7. Use super().__init__(fname, lname)
#    to call the constructor of the parent class.

# 8. Store the year in a variable named:
#    self.graduationyear

# 9. Create an object of the Student class with:
#    first name, last name, and graduation year.

# 10. Call the printname() method to display the full name.

# 11. Print the graduation year also.

# Example Output:
# Joey King
# 2021
"""
Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display 
the full name.
Create a child class Student (attributes - fname, lname, year). 
Access the attributes of parent class in child class using super() function. 
Then, create an object for the child class and call the display method to display the full name. 
Also, print the graduation year.
"""
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,year):
        self.year = year
        super().__init__(fname,lname)
o = Student("Liam","Jose",2011)
o.printname()
print(o.year)