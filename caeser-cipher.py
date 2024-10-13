'''
Using Functions to Implement a Caesar Cipher
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