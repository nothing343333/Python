# a class is a blueprint for creating objects that havew attributes and methods it acts as a template for creating objects with similar characteristics.
# function in class is called a method

# creating a simple class
# class HuXn:
#     def __init__(self) -> None:
#         self.name = "Jordan"
#         self.age = 20
#         self.location = "US&A"
#     def talk(self):
#         # print("Hey my name is Jordan")
#         print(f"Name: {self.name}, Age:{self.age} Location: {self.location}")
#     # method (function)


# # instance/Object
# Jordan = HuXn()
# Jordan.talk()
# self define kr dena wrna error dega


# 2. __init__ is a constructer which allow us to create variables in class






# static variable
class car:
    num_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    # accessing static variable
        car.num_cars +=1

car1 = car("Toyota", "Camry")
car2 = car("Seman", "Lurk-9")

print("Number of cars created: ", car.num_cars)