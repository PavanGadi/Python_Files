# '''
# ..................... " Sets " .............................
# The elements in the set cannot be duplicates.
# The elements in the set are mutable(can be modified).
# There is no index attached to any element in a python set. 
# So they do not support any indexing or slicing operation.
# We can add or remove items from it.
# defined with {}
# A set is created by placing all the(elements)inside curly braces {},
# separated by comma , or by using the built-in set() function.

# '''
# # list()
# # set()
# # dict()
# # tuple()

# # sekhar={1,2,2}
# # print(type(sekhar))

# # shiva=set()
# # print(type(shiva))

# # l=[1,1,2,3,4,4,5,65]
# # s=set(l)
# # print(s)











# '''
# add
# remove
# discard
# clear
# copy
# update
# '''
# kishor={1,2,1,2,3,4,5,6,9,8,7,6,5,4}
# # print(kishor)
# # kishor.add(11111)
# # print(kishor)
# # kishor.remove(10000000000)
# # kishor.discard(10000000000)
# # kishor.update([22,33,44,55,666,888,99,000])
# # print(kishor)










# # set operations
# '''
# Union
# intersection
# difference
# symmetric difference

# isuperset
# issubset
# isdisjoint
# '''

# # vamsi={1,2,3,4,5,6,7,9}
# # ganesh={1,2,3,4,5,6,7,8}

# # print(vamsi.union(ganesh))   # +

# # print(vamsi.intersection(ganesh))

# # print(vamsi.difference(ganesh))
# # print(vamsi.symmetric_difference(ganesh))


# # s={0}
# # s1={1,2,3,4,7}
# # print(s.isdisjoint(s1))


# # kishor={1,2,1,2,3,4,(5,6,9),8,1+2j}
# # print(kishor)


# # for naveen in kishor:
# #     print(naveen)

# '''
# #task 13

# hotel management


# # task 14
# date time module

# # task 15

# total set practice

# '''



# print(' Welcome to Sandeep Hotel ')
# customer_name=str(input('Enter the Customer Name:'))
# print('How can i help you {}'.format(customer_name))
# benifits="""
#           1.Rooms
#           2.Wifi
#           3.Meals
#           4.currrent
# """
# hotel_prices={'single_Room':1000,"Double_Room":2000,'Meals':1000,"current":100}
# while True:
#     choose=input('Choose Something for benifits 1 and for rates 2:')
#     if choose=='1':
#         print(benifits)
#     else:
#         s=str(hotel_prices)
#         b=s.replace('{',"")
#         c=b.replace('}',"")
#         a=c.replace(',','\n')
#         d=a.replace("'",'')
#         print(d)


# # s="this {is} book {is}".format(a="are")

# a==b
# a!==b
# a<=b
# a>=b

# a=1
# b=2
# if a>b:
#     print("a is smaller than b")
# elif a<b:
#     print("a is smaller than b")
# else:
#     print("b is smaller than a")



