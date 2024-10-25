def reversed_word(sentence):
    reversed_sentence = ''
    word=''
    words = []

    for char in sentence:
        if char == ' ':
            if word:
                words.append(word)
                word = ''
        else:
            word+=char
    if word:
        words.append(word)

    for i in range(len(words)-1, -1, -1):
        reversed_sentence += words[i]

        if i != 0:
            reversed_sentence += ' '

    return reversed_sentence

print(reversed_word('Today is a good day'))