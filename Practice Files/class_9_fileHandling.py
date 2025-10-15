# What is file Handling
# Python file operations such as Opening,Reading,Writing,Closing,Renaming and Deleting comes under
# File Handling 

# Modes of file
# r  - read
# w  - write
# a  - append
# r+ - read and write
# w+ - write and read

# Functions
# Read  - Total data read
# Write - Write data
# readline - Reads first line
# readlines - used to change string to list
# writelines - used to change list to string
# seek  - Change the position of the pointer
# tell  - used to tell the current position of the pointer 

# Use this to check if the file exists in current working directory, if not use the abslote path as in the below code

# import os
# print("Current working directory:", os.getcwd()) 


a=open(r"e:\Python\Practice Files\test.txt", mode="r")  # Using r"..." tells Python: “Don’t treat backslashes as escape characters. Just take the string as-is.”
b=a.read()
print(b)
a.close()

# Using With open.
# This helps to auto close the file

with open (r"e:\Python\Practice Files\test.txt", mode="r") as f:  
    print(f.readlines())

# To Print only a selected line
with open(r"e:\Python\Practice Files\test.txt", mode="r") as f:
    a = f.readlines()
    print(a[4])

# Also the above code can be written like below
# The below code provide an example for Exception Handling
try:
    with open("test.txt", "r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("❌ The file does not exist. Please check the path.")
except PermissionError:
    print("❌ You don’t have permission to read this file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")


# Write and Append Mode
# We can also open the file in write mode and add anything if we do like that all the old data in the file
# will be lost and new data will be added. Insated we use append mode
# a,w,a+ and w+ can also create a file if that file does not exist

with open (r"e:\Python\Practice Files\test.txt","a") as f:  
    f.write("\nThis is write function")

with open (r"e:\Python\Practice Files\test.txt","a+") as f:
    print(f.tell())
    f.write("This is w+ function")
    print(f.tell())



