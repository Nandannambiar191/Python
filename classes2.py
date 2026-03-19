"""

Write a program to create a class with name Student and perform the following tasks - 
Create a class variable grade and name 
Create a function to print a sentence 
Create a function to print 
class variables grade and 
name Create an object of class Student Call the two functions to execute them
"""
class  Student:
    grade = 100
    name = "Nandan"
    def abc(self):
        print("Hi, I am a student")
    def xyz(self):
        print(f"My name is {self.name} and I am in grade {self.grade}")
r = Student()
r.abc()
r.xyz()