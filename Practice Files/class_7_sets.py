a = {100,1,1,1,2,3,3,3,3,3,3,55,3,4,5}
print(type(a))

print(a)        # This will not print in the given order as sets are unorderd
# a[4] = 99.9   # We can cannot add elements based on index as sets do not have index


print(a)        # the duplicates from the set are removed and remaining elements are printed   


# Set Operations

x = {1,2,3,4}
y = {4,3,5,6,7}

print(y.union(x))
print(x.union(y))

