#!/usr/bin/env python3

# date: 2019 Nov 6

class Person:
    """Docstring: This is my Person class"""

    def __init__(self, name, age):
        self.name = name
        self.age  = age
    # end of __init__()

    def greeter(self):
        print("\t Hello my name is ",  self.name)
    # end of greeter()

    def getAge(self):
        print("\t  Again, my name is ",self.name, "my age is the following: ", self.age)
# end of Person class


##### Initialize the class ######
p1 = Person("John Watson", 26)
p1.greeter()
p1.getAge()


p2 = Person("Sherlock Holmes", 27)
p2.greeter()
p2.getAge()
