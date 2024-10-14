'''
Categorizing Values

With Python, we can mix types in a list. 
In this lab, we will create a list with different types and print the values.

In this lab, we will:

 - Use numeric data types
 - Use string data types
 - Use the list data type
 - Use a for loop
 - Use the print() function
'''

myMixedTypeList = [45, 290578, 1.02, True, 'My dog is on the bed.', '45']

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))