'''
Working with Numeric Data Types

Python makes it easier to do math. 
In fact, Python is a popular language among data scientists, who must analyze large amounts of data. 
In this lab, we will explore the basic data types that are used to store numeric values.

In this lab, we will:

 - Use the Python shell
 - Use the int data type
 - Use the float data type
 - Use the complex data type
 - Use the bool data type
'''

print("Python has three numeric types: int, float and complex")

myValue=1
print(myValue)

print(type(myValue))

print(str(myValue) + " is of the data type " + str(type(myValue)))


myValuee=3.14
print(myValuee)
print(type(myValuee))

print(str(myValuee) + " is of the data type " + str(type(myValue)))


myVal = 5j
print(myVal)

print(type(myVal))

print(str(myVal) + " is of the data type " + str(type(myVal)))

myBool = False

print(myBool)
print(type(myBool))

print(str(myBool) + " is of the data type " + str(type(myBool)))