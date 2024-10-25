def prime_numbers(start, end):
    prime_numbers=[]

    for num in range(start,end):
        if num > 1:
            is_prime = True

            for i in range(start+1, int(num**0.5)+1):
                if num%i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

print(prime_numbers(1,100))
                
    