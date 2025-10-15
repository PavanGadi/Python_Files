a = 'pavan'
b = "pavan"
c = '''pavan'''

print(type(a), type(b), type(c))

# Methods
# Upper / Lower
a = 'pavan'
b = 'PAVAN'
print(a.upper())
print(b.lower())

# Count
a='pavan'
print(a.count('a'))
b='why what and why what are are are and'
print(b.count('are'), b.count('why'))

# Find / Index
a='My Name is Pavan Kumar Gadi'
print(a.find('Pavan'))
print(a.find('Hello'))
# print(a.index('Hello'))

# isalnum
a="1234"
print(a.isalnum())

# Replace
a="Hi Hello How are you?"
print(a.replace("Hi","hello!!"))

# Split
a="Hi Hello How are you?"
print(a.split())