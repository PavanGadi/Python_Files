a=[1,9,9,99,0,'True',0.1,[1,2,4]]
print(type(a))
print(a[4] ,a[7])
print(a[0:5:2])

#Slicing
a=[1,2,3,5.5,0,12]
print(a[0:4:2]) # As the stop value is 0 it will not be shown in the output

a=[1,2,3,5.5,0,12,100]
print(a[0:5:2])
print(a[5:0:-2])
print(a[5:0:2]) # This is will show empty o/p as we are going in backwad direction so step/skip should be negative
print(a[:5]) # This will print all the data before the index 5
print(a[5:]) #  This will print all the data after the index 5
print(a[:]) # If we give : / :: it will give total data in the list
print(a[:-1]) # This will skip the last digit and give the o/p , else if we give :: the list will be reversed
print(a[-1:]) # This will print only last digit


a=[1,2,3,4,5,6,7]

# Appemd
a.append([9]) # This will in the form of sub list in the given list
a.append(9) # This will just add the data at the end

# Extend
#a.extend(9) # This will not work as extend requires the data to be given in specific format
a.extend([1]) # This wil work
print(a)
a.clear()
print(a)

# Copy
a=[1,2,3,4,5]
b=a.copy()
a.append('abc')
print(b)
print(a)

#Insert
a=[1,2,3,4,5]
a.insert(0,"abc")
print(a)
