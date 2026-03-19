"""

Write a program to create a class Parrot and perform the following tasks - 
Create a class variable species Create a constructor that has instance variables - name and age 
Create instance methods for this class named sing and dance, making them print a message. 
Create instances of class Parrot, passing arguments as well Print Class variable by accessing 
it Print Instance variables as well
"""
class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self,song):
        self.song = song
        print(f"{self.name} sings {self.song}")
    def dance(self):
        print(f"{self.name} is dancing")
y = Parrot("Blu",6)
print(f"{y.name} is a {y.species} that is {y.age} years old")
y.sing("Happy Birthday")
y.dance()
