'''
Using Functions to Implement a Caesar Cipher

In programming, a function is a named section of a program that performs a specific task. 
Python has built-in functions like print() that are provided by the language. 
Additionally, we can use functions provided by other developers through the import statement. 
For example, we can use import math if you want to use the math.floor() function. 
In Python, we can make your own functions, which are called user-defined functions.

To drive the discussion of user-defined functions, we will write a program that implements a Caesar cipher, which is a simple method of encryption. 
A Caesar cipher takes the letters of a message and shifts each letter along the alphabet by a certain number of places.

In this lab, we will:

 - Create user-defined functions
 - Use several functions to implement a Caesar cipher encryption program
'''

# creating a user defined function
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
# alphabet = 'ABC'
# print(getDoubleAlphabet(alphabet))

# Encrypting a message
def getMessage():
    stringToEncrypt = input('Please enter a message to encrypt: ')
    return stringToEncrypt
    
# Getting a cipher key
def getCipherKey():
    shiftAmount = input('Please enter a key (whole number from 1-25): ')
    return shiftAmount
    
# Encrypting a message
def encryptedMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Decrypting message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptedMessage(message, decryptKey, alphabet)

# Creating main function
def runCaesarCipherProgram():
    myAlphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(f'Alphabet: {myAlphabet}')
    
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(myMessage)
    
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    myEncryptedMessage = encryptedMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decryted Message: {myDecryptedMessage}')
    
    
runCaesarCipherProgram()