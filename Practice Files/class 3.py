# 
a=11
b=90
c=b//a
d=b%a
e=b/a
print(c,d,e)


## COnditional Statements
if 2>1:
    print("2 is greater than 1")
    if 2:
        print("2 is even")
    else:
        print("2 is odd")
else:
    print("2 is less than 1")

## Short Hand If Else
a=1
b=2
print("b is greater") if a<b else print("a is greater")

# Short hand if
if 5>2 : print("5 is greater than 2")

# Loops
a=10
while a<20:
    print("Curret value of a is",a)
    a+=1

for i in ("pavan kumar gadi"):
    print(i, end=" ")   # End is used to print Horizantally
print()                 # This is given after the loop to seperate the each loop with the other loop

for i in range(10):
    print (i, end=" ")
print()

for i in range(0,100+1):  # As we cannot use less than or equal to in range, if we want last value also to print we need to use +1
    print(i, end=" ")
print()

for i in range(0,100,3):  
    print(i, end=" ")
print()