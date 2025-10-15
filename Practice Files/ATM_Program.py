# This sample program using global varaible

menu = '''
    1. Credit
    2. Debit
    3. Current Balance
    4. exit

'''

a = "pavan"
b = "Gadi@123"
c = 15000    # Everythime this amount will only be used, We can enchnace this by using functions

username = input("Enter the username ")
password = (input("Enter the password "))


if a == username and b == password :
    while True:

        print(menu)

        option = int(input("Select the options "))
        if option == 1:
            credit = float(input("Enter the credit amount : "))
            print("The Balance amount is :", c+credit)
        
        elif option == 2:
            if c < 0:
                debit = float(int("Enter th debit amount: "))
                print("The Balance amount is :", c-debit)
            else :
                print("Not enough balance to be debited")
        
        elif option == 3:
            print(c)
        
        elif option == 4:
            break
else :
    print("Incorrect Credentials")