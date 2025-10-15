# krishna=[] # empty list
# krishna=list()
# print(type(krishna))


# krishna=[1,2.2,'python',True] # method 1
# krishna1=list([1,2.2]) # method 2
# print(krishna)
# print(krishna1)




# sandeep=[2.2,3.4,5.5,1,2,3,4,5]
# print(sandeep[-1])


# james_bond=[7,3,5,3,34,64,2.4,32,5,35,35]
# # slicing
# #[start:stop:skip]
# # print(james_bond[0:5+2])
# print(james_bond[::-1])


# james_bond=[7,3,5,3,34,64,2.4,32,5,35,35]
# james_bond[0]="kiran"
# print(james_bond)



# variable.method()
# aparna.append([123])
# print(aparna)
# # aparna.extend([123])
# print(aparna)
# print(aparna.count(1))


# print(aparna.index(4525))



# print(len(aparna))
# print(aparna.index(1))
# aparna.clear()
# print(aparna)
# b=aparna.copy()
# aparna.append('abc')
# print(b)




# aparna.insert(0,"kiran")
# print(aparna)

# aparna.pop(0)
# aparna.remove(1)
# print(aparna)
# aparna.reverse()
# print(aparna)

# c=[1,3,4,4,421,42,4231,4,442,4]
# c.sort(reverse=True)
# print(c)











str1 =[1,6,6,6,6,6,6,6,6,6,6,6,6,2,4,5,5,6,3,3,3] 
n=[] 
for i in str1:
     print(i)
     if i==6:
        str1.remove(6)
     else:
         n.append(i)
     print(n)






# s=[1,2,3,4,3,4]
# for i in range(len(s)):
#     if s[i]==3:
#         print(i)















# for i in range(10):
#     if i%2==0:
#         print('even')
#     else:
#         print('odd')





# list = ["EVEN" if i % 2 == 0 else 'odd' for i in range(10)]
# print(list)








# # #syntax
# # list=[expression if con for item in sequence]











# newlist = []
# for x in ["apple", "banana", "cherry", "kiwi", "mango"]:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)














# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)




'''
Task 10
practice list and list comp
Task 11
prepare a doc on list
Task 12
explore jira

'''
s=[1,2,3,4,5,5,76,7,8,8]
print(s[0:11:2])