class Pavan():                              # This is class definition
    def kumar(self):                        # Here in this method the first parameter should be Self
        return("This is a class")

gadi = Pavan()              # This is Object creation  -->  object_name = Class()
print(gadi.kumar())         # To access method in the class --> object_name.method

class Maths():
    c = 100
    def sum(self,a,b):
        return(a+b)

input = Maths()
output = Maths()
print(output.c)
print(input.sum(10,20))
print(output.sum(100,321))


# __init__
# It is automatically called whenever you create an object from a class.
# Its main job is to initialize the object’s attributes (variables).
# By using this we can use the variables defined in one function into another function in the same class
# We will send the data to the methods from object creation

class Car():
    def __init__ (self,tata,suziki):
        self.a = tata
        self.b = suziki
    def output(self):
        print(self.a,self.b)

car1 = Car("nexon","swift")
car1.output()

# Another example for __init__
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee created:", name)

e1 = Employee("John", 50000)
e2 = Employee("Alice", 60000)

print(e1.name, e1.salary)
print(e2.name, e2.salary)
