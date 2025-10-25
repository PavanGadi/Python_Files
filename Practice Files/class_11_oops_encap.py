# Encapsulation means wrapping data (variables) and methods (functions) into a single unit, 
# i.e., a class — and restricting direct access to the data from outside.

# In simple words:
# 🧱 Encapsulation = Data Hiding + Data Protection

# Encapsulation is the concept of keeping the internal details of an object hidden from the outside world 
# and providing controlled access through methods.

# Binding of class
# public        ----> Everyone can access
# private __     
# protected _   ----> Only Inherited can access

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary  # private variable

# emp = Employee("Pavan", 50000)
# print(emp.name,emp.__salary)  # The variable __salary is private — not accessible directly from outside.

# We can overcome this by using getters and setter
# The variable is protected — you can’t modify it directly,
# but you can modify it only through controlled methods.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private variable

    # Getter method
    def get_salary(self):
        return self.__salary

    # Setter method
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary amount")

emp = Employee("Pavan", 50000)
print(emp.get_salary())  # Accessing via getter

emp.set_salary(60000)    # Updating via setter
print(emp.get_salary())

emp.set_salary(-1000)    # Invalid input test



