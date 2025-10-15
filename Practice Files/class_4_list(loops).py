str1 =[1,6,6,6,6,6,6,6,6,6,6,6,6,2,4,5,5,6,3,3,3] 
n=[] 
for i in str1: 
    print(i) 
    if i==6: 
        str1.remove(6) 
    else: n.append(i) 
    print(n)   # In this program the code is skipping the last three

# Alternate Ways
str1 = [1,6,6,6,6,6,6,6,6,6,6,6,6,2,4,5,5,6,3,3,3]
n = []
for i in str1[:]:  # `[:]` creates a copy
    if i != 6:
        n.append(i)
print(n)

# str1 = [1,6,6,6,6,6,6,6,6,6,6,6,6,2,4,5,5,6,3,3,3]
# n = [i for i in str1 if i != 6]
# print(n)

# Explanation why it skips one element

# The code skips the last because here were are passing the values instead of indexes, But internally python iterates over
# indexes, So when we removed last 6 in the list the three in the list will come into 6 index, As python already removed 
# that index it will skip that 3 and last two threes are prined.


# Here's how it breaks down:

# Syntax	                            Iterates over	       Access to Index?
# for i in list:	                    Values	               ❌ No
# for i in range(len(list)):	        Indices	               ✅ Yes
# for idx, val in enumerate(list):	    Both Index & Value	   ✅ Yes

# 🧪 Example: Removing 6 While Iterating
# Here’s a small piece of code with detailed print statements that show how Python internally skips elements:

# python
# str1 = [6, 6, 2, 6, 3]
# print("Original list:", str1)

# for i in str1:
#     print("Current value:", i)
#     if i == 6:
#         str1.remove(6)
#     print("List after removal:", str1)
# 🧠 What Happens Step-by-Step
# Let’s walk through this manually:

# Starts with str1 = [6, 6, 2, 6, 3]

# First value is 6 → removed → list becomes [6, 2, 6, 3]

# Second value is now 2 (because the list shifted) → not removed

# Third value is 6 → removed → list becomes [6, 2, 3]

# Fourth value is 3 → not removed

# Loop ends. But notice: one 6 was skipped!

# 🧯 Why It Skips
# When you remove an item, all elements shift left, but Python's internal position counter keeps incrementing as if nothing changed. So it ends up jumping over elements.
