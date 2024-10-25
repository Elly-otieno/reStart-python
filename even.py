def getEvenNumber(start, end):
    even_number = []

    for num in range(start, end):
        if num % 2 == 0:
            even_number.append(num)

    print(even_number)

getEvenNumber(10, 70)
