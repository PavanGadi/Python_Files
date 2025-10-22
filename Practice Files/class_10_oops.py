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