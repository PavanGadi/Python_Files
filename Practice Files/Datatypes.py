#Split
a = "abc,defhij"
Split = a.split(",")
print ("After splitting = ", Split[1] )

name = "Pavan Kumar Gadi"
uppercase = name.upper()
lowercase = name.lower()
print("Uppercase = ", uppercase)
print("Lowercase = ", lowercase)

#Concatination
a = "Pavan"
b = "Kumar"
c="Gadi"
result =a+" "+b+" "+ c
print("Concatnated String : " , result)

#To find the string length
a = "Pavan Kumar Gadi"
b = len(a)
print("The length of string is : ", b)

#Replace
a = "This a new World"
b = a.replace ("World" , "Earth")
print("Text after replacing = ", b)

#Substring
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
else :
    print(substring, "Not found in the text")

