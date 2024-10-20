prime_numbers = []

for x in range(1, 126):
    if x > 1:
        is_prime = True

        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(x)

print(prime_numbers)
