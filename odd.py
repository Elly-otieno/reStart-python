def getOddNumber(x,y):
    odd_numbers = []

    for num in range(x,y):
        if num % 2 != 0:
            odd_numbers.append(num)

    print(odd_numbers)

getOddNumber(10, 70)