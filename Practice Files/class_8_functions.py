def a() :
    print("This is a Function")
a()

def sum(a,b) :
    print(a+b)                 # We can write print inside the function
sum(5,32.96357)

#####################################################################################################3
# The difference btw print and return is 
# Print displays output on screen, where as Retrun gives the values back to function
# When print is used output cannot be reused, Returned value can be stored in a variable that can be reused
#  Example:
def demo_print():
    print("Hello")
    
def demo_return():
    return "Hello"

x = demo_print()   # prints "Hello"
y = demo_return()  # returns "Hello"

print("x:", x)  # x: None          # We can see that when we are reusing the value given by print it is returning none
print("y:", y)  # y: Hello

############################################################################################################

def mul(a,b) :
    print("The product of a and b is : ", a*b) # This will not take as a tuple because comma in print is aurgment seperator where as comma in return is tuple constructor
mul(5,5)

def add(a,b) :
    return "The sum of a and b is : ",a+b #Python takes this as a Tuple as we have seperated using comma and that is why this is returing as a tuple(O/p has brackets)
print(add(50,33))                         # If we write return inside the function we need to print the function


def add(a,b) :
    return f"The sum of a and b is : {a+b}"
print(add(33,20))

def sub(a,b) :
    return "The difference of a and b is : " + str(a-b)
print(sub(99,99))


def div(a,b) :
    return f"The division of {a} and {b} is : {b/a}"   # Anything inside {} is treated as a Python expression.That expression is evaluated at runtime.The result of that expression is converted to a string (using str()) and inserted into the final string.
x = int(input ("Enter the value of a : "))
y = int(input ("Enter the value of b : "))
print(div(x,y))


# # Lambda Function

# p = lambda a,b,c : a*b    # This should have only one expression like a+b+b+c // a-b+c // a*b+c. This will not have accept (a+b+c)(a*b+c) as this is a cpmbination of two expressions.
# print(p(1,2,3))

# Filter
# This will only take the data which is true
# There will be no change in data

# filter() does not create a list directly (for efficiency).

# Instead, it creates an iterator that will generate the values one by one when you loop over it.

# That’s why printing b directly only shows the object’s memory location, not the contents.

def advfilter(p):
    if p >= 18:
        return True
    else:
        return False

p = [10,18,24,32,97,1]
b = filter(advfilter,p)
print(list(b))  # If we do not use the list in this print it will only print the memory location not the values

# Map
# There will be change in the data structure, Transforms each element.

def addition(q):
    return q+2

q = [1,2,3,4,5]
r = map(addition, q)
print(tuple(r))


# Reduce

from functools import reduce
z = [1,2,3,4,5]
x = reduce(lambda a,b : a*b , z)
print(x)

# Imagine you have fruits in a basket 🍎🍌🍇

# filter() → Pick only bananas 🍌

# map() → Peel all fruits 🍌🍎🍇 → 🍌(peeled)🍎(peeled)🍇(peeled)

# reduce() → Make a fruit salad 🥗 (combine everything into one)
