'''
Working with Lists, Tuples, and Dictionaries

In Python, string and numeric data types are often used in groups called collections. 
Three such collections that Python supports are the list, the tuple, and the dictionary.

In this lab, we will:

 - Use the list data type
 - Use the tuple data type
 - Use the dictionary data type___
'''

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))


print(myFruitList[0])

print(myFruitList[1])

print(myFruitList[2])


myFruitList[2] ="orange"

print(myFruitList)

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])


myFavouriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple",
}

print(myFavouriteFruitDictionary)

print(type(myFavouriteFruitDictionary))

print(myFavouriteFruitDictionary["Akua"])

print(myFavouriteFruitDictionary["Saanvi"])

print(myFavouriteFruitDictionary["Paulo"])
