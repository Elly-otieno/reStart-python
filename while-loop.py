'''
Working with Loops

A loop is a segment of code that repeats. 
We will be introduced to two types of loops: the while loop and the for loop.

In this lab, we will:

 - Use a while loop
 - Use a for loop
'''

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it")

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn`t it. Try again".format(guess))
    
