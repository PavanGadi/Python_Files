# Polymorphism
# Method Overloading.............................................................

# class Poly():
#     def values(self,a,b,c):
#         print(a,b,c)

# mo=Poly()
# mo.values(1,2,3)
# mo.values(1,2)           # Here we are not passing any values to the c but we have defined c in method
# mo.values(1) 

# To fix the above kind of error we can pass default arguments

class Poly():
    def values(self,a=None,b=None,c=None):
        print(a,b,c)

mo=Poly()
mo.values(1,2,3)
mo.values(1,2)           
mo.values(1) 

# Or We can achieve through Variable-length arguments (*args)

# *args collects all positional arguments into a tuple.

# So no matter how many values you pass, they get packed into args.

# Call	What args contains	Output
# mo.values(1,2,3)	(1, 2, 3)	(1, 2, 3)
# mo.values(1,2)	(1, 2)	(1, 2)
# mo.values(1)	(1,)	(1,)
# mo.values()	()	()

class Poly_2():
    def values(self,*arg):
        print(arg)

mo=Poly_2()
mo.values(1,2,3)
mo.values(1,2)           
mo.values(1) 

# Method overriding...........................................
# Here, both classes have a method parent().
# When you call Output2.parent(), Python uses the child class version, not the parent’s.

class Mor_1():
    def parent(self):
        print("This is parent class")

class Mor_2(Mor_1):
    def parent(self):
        print("This is child class")

Output1=Mor_1()
Output2=Mor_2()
Output1.parent()
Output2.parent()

# The super().sound() line allows you to first call the parent class version
# then add child-specific behavior.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()      # calls parent class method
        print("Dog barks")
        

d = Dog()
d.sound()

# Inheritance + Method Overriding + Polymorphism

class Animal:
    def sound(self):
        print("Animal makes some sound")

# Each subclass inherits from Animal.
# Each subclass overrides the sound() method to give its own version.

class Dog(Animal):
    def sound(self):       # overriding the parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):       # overriding the parent method
        print("Cat meows")

class Cow(Animal):
    def sound(self):       # overriding the parent method
        print("Cow moos")

# The same method name sound() is called for each object.
# But depending on the object’s actual class, the appropriate version of the method runs.
# This is Polymorphism — “one interface, many forms.

# Create objects of different animal types
animals = [Dog(), Cat(), Cow()]

# Loop through and call the same method
for animal in animals:
    animal.sound()
