a={
    "Pavan":"Gadi",
    1:10,
    2.0:"Hello!!",
    3:["a","b","c","d"]
}
# print(type(a))
# print(a[3])

# a["Pavan"] = "Hiii!!"  # Used to update the value in a Dictionary
# print(a)

# # Methods

# # Get()
# print(a.get(1)) # We can also print without method like in the line 8. But 

# # update
# a.update({1:11})
# a.update({4:5})
# print(a)

# # POP
# a.pop(4)
# print(a)

for i in a.items():            # This will give o/p in tuple format        
    print(i)

for i,j in a.items():        
    print(i,j)