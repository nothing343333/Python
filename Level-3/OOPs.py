# POP Produce oreinted programming 
# functions and definations use hote hai not objects 

# OOPs object oreinted programming
# classes and objects use hote hai not functions
# is a programming paroday where the software desgin revolves around objects or data rather than functions.

# why use OOPs?
# it helps to mimick real world enetities and their intractions.
# code can be  resued and helps in organization and maintainability of code.
# where we have complex system and code repos we use OOPs 
# easy padta hai


# classes and objects
# classes
# user defined datatypes and a blueprint to create an object.
# print("hello")
# object
# an instance of type class
# mimick real life entities

# class student:
#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name
    

# student1 = student()
# student1.set_name("HuXn")
# print(student1.get_name())


# student2 = student()
# student2.set_name("FuXn")
# print(student2.get_name())



# make a class of rectangle
# class Rectangle:
#     def set_dimension(self, height, width):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    


# rectangle1 = Rectangle()
# rectangle1.set_dimension(4, 3)
# print(rectangle1.area())
# print(rectangle1.perimeter())



# attributes
# class 
# defined under the class
# all object instances will have these attriubtes

# instance
# are specific to a particualr instance or object



# access modifiers
# prublic
# protected
# private
# controls the access of the class attributes and functions


# public
class ABC:
    def __init__(self):
        self.public_attibute = None 
        self.__private_attibute = None
        self._protected_attibute = None

        
    def public_function(self):
        pass

obj1 = ABC()
obj1.public_function()
obj1.public_attibute

obj2 = ABC()
# obj2.__private_attibute()
# error aya coz attribute private hai

obj3 = ABC()
obj3._protected_attibute()