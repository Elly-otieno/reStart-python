def palindrome(word):
    reversed_word = ''

    for char in word:
        reversed_word = char + reversed_word

    if reversed_word == word:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')

palindrome('madam')
palindrome('hello')
