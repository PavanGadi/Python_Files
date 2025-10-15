
'''

A lambda function is a small anonymous function.

A lambda function can take any number of arguments,
 but can only have one expression.

lambda arguments : expression

'''


# x = lambda a,b,c : a + b + c
# print(x(5,2,1))












# l1=[12,34,5,6,8] # list
# l2=[] # empty list
# for i in l1: # li=[12,34,5,6,8] 
#     t=lambda a : a+1
#     l2.append(t(i))
# print(l2)















'''
The filter() method filters the given sequence with the help 
of a function that tests each element in the sequence 
to be true or not.

'''
'''
syntax:

filter(function, sequence)
Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered.

'''

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x >= 18:
#     return True
#   else:
#     return False

# adults = filter(myFunc, ages)
# print(list(adults))





'''
Generator-Function : A generator-function is defined like a normal function,
but whenever it needs to generate a value, 
it does so with the yield keyword rather than return.
If the body of a def contains yield, the function automatically
becomes a generator function.
'''













# A Python program to demonstrate use of
# generator object with next()

# A generator function
# def simpleGeneratorFun():
# 	yield 1
# 	yield 2
# 	yield 3

# # x is a generator object
# x = simpleGeneratorFun()

# Iterating over the generator object using next
# print(x.__next__()) # In Python 3, __next__()
# print(x.__next__())
# print(x.__next__())










'''
The yield statement is responsible for controlling the flow of the generator function.
It pauses the function execution by saving all states and yielded to the caller. 
Later it resumes execution when a successive function is called. We can use the multiple yield statement in the generator function.

The return statement returns a value and terminates the whole function and only one return statement can be used in the function.
'''

# def aa():
#     return 1+1
#     return 2+1
# print(aa())























'''
The python map() function is used to return a list of results
after applying a given function to each item of an iterable(list, tuple etc.)

map(function, iterables)  
'''



















# def calculateAddition(n):  
#   return n+n  
  
# numbers = (1, 2, 3, 4)  
# result = map(calculateAddition, numbers)  
# print(list(result))



















'''
The reduce() function, as the name describes,
applies a given function to the iterables and returns a single value.
'''







# def add(*a):
#     return a+a
# add(1,2,3,4,5,67,8,5)








# from functools import reduce
# # reduce(function,sequence)
# d=reduce(lambda a,b: a+b,[23,21,45,98])
# print(d)







# def even(x):
#     if x%2==0:
#         print(x)
#diff bw filter and map
# nums = [11, 22, 33, 44, 55]
# map = list(map(lambda x: x**2, nums))
# print(list(map))
# filter = list(filter(lambda x: x%2==0, nums))
# print(filter)



# a=1
# b=2
# def add(a,b):
#     return a+b
# add(1,2)




'''

Task 22
practice function and advance functions
Task 23
write a python program using atm and calculator
Task 24
complete mini project                   


                    '''


# a="kiran"
# s=lambda d:d*10
# print(s(a))



def suresh(a,b):
    print(a*b*a*b*a)
suresh(1,2)