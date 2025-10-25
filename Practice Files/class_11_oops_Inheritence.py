# Single Inheritence
# In this parent properities are inherited to child. 
class Parent():                                     
    def output_parent(self):
        print("This is parent class")

class Child(Parent):
    def output_child(self):
        print("This is child class")

obj = Child()                     # We need define objec to child class as parent prperties are pased
obj.output_child()                # to child class and we can use methods in both the classes.
obj.output_parent()


# Multiple Inheritence(
# This is Multiple Inheritence as child is getting properties from two parent classes(Father,Mother)
class Father_M():
    def output_parent(self):
        print("This is Multiple father Inheritnce")

class Mother_M():
    def output_mother(self):
        print("This is Multiple mother Inheritnce")

class Child_M(Father_M,Mother_M):
    def output_child(self):
        print("This is Multiple child Inheritnce")

obj_m = Child_M ()
obj_m.output_child()
obj_m.output_mother()
obj_m.output_parent()


# Multi Level Inheritence
# This is Multi Level Inheritence
class Grandfather_ML():
    def output_grandfather(self):
        print("This is Multi Level Grandfather Inheritnce")

class Father_ML(Grandfather_ML):
    def output_father(self):
        print("This is Multi Level father Inheritnce")

class Child_ML(Father_ML):
    def output_child(self):
        print("This is Multi Level child Inheritnce")

obj_ml = Child_ML()
obj_ml.output_grandfather()
obj_ml.output_father()
obj_ml.output_child()

# This is Hirerachial Inheritence
# This will have one parent class and two child classes

class Parent_H():
    def output_parent(self):
        print("This is hparent inheritence")

class child_1(Parent_H):
    def output_child1(self):
        print("This is hchild1 inheritence")

class child_2(Parent_H):
    def output_child2(self):
        print("This is hchild2 inheritence")

objh1=child_1()
objh2=child_2()
objh2.output_child2()
objh2.output_parent()
objh1.output_child1()
objh1.output_parent()