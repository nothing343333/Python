class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self): # agar self define nhi hoga to ek argument accepted batayega but 0 arguments leta hai
        print(f"The language is {self.language}, and salary is {self.salary}")



harry = Employee()
harry.language = "C"  #default python hai but update krke c kr skte hai
harry.salary = 12 # This is a instance attribute
# print(harry.language) # will print out c
# print(harry.salary) will print out 12
harry.getInfo()
# Employee.getInfo(harry) same hi hai dono