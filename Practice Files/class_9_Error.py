try:
    # risky code 
    print("a")

except:
    print("error vachindi")
else:
    print("error raledu")
finally:
    print("always")





try:
    print('a'+10)
except Exception as kiran:
    print("Error occured",kiran)
# except:
    print("Error occured")



try:
    print('a'+10)
except:
    print("outer")
    try:
        print(a)
    except:
        print("inner")





if True:
    print("this is")




s=str(1)+"d"
print(s)

d={1:"a"}
print(d[2])


c=[1,2,3,535,5]
print(c[100])

while True:
    print("loooop")



def credit(a,b):
    return a+b

def debit(a,b):
    return a-b

def mini(a,b):
    return a*b

op=int(input("Enter the option"))
a='''
   1.add
   2.sub
   3.mul

'''
if op==1:
    add()
elif op==2:
    sub()

