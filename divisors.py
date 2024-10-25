num = int(input('Enter a number you want its divisors: '))

x = range(1, num+1)

for elem in x:
    if num%elem == 0:
        print(elem)