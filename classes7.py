# 1) Import the ABC tools:
#    a) Import `ABC` and `abstractmethod` from the `abc` module.

# 2) Create an abstract base class:
#    a) Make a class that inherits from `ABC`.
#    b) Create an abstract method `move()` (meant to be overridden).

# 3) Create multiple child classes:
#    a) Each class should inherit from the base class.
#    b) Each class must implement `move()` with its own print message.

# 4) Create objects and call `move()`:
#    a) Make an object for each child class.
#    b) Call the `move()` method to show different outputs.

"""
Write a program to implement abstraction on animal class (base class). 
The abstract method will be move that is for displaying what subclasses can do.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk.")
class Snake(Animal):
    def move(self):
        print("I can slither.")
class Dog(Animal):
    def move(self):
        print("I can walk as a dog.")
class Lion(Animal):
    def move(self):
        print("I can walk as a lion.")
h = Human()
s = Snake()
d = Dog()
l = Lion()
h.move()
s.move()
d.move()
l.move()