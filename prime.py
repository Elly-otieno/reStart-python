def prime_numbers(start, end):
    prime_number = []

    for number in range(start, end):
        if number > 1:
            is_prime = True

            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_number.append(number)
    with open('results.txt', 'w') as file:
        for number in prime_number:
            file.write(f'{number}\n')


prime_numbers(1, 251)
                
    