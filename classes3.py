"""

Write a program to create a class Parrot and perform the following tasks - 
Create a class variable species 
Create a init method that has instance variables - name and age 
Create instances of class Parrot, passing arguments as well 
Print Class variable by accessing it Print Instance variables as well
"""
class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
y = Parrot("Blu",6)
i = Parrot("Jack",9)
print(f"{y.name} is a {y.species} that is {y.age} years old")