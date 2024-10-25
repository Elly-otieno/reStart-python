def get_number(a:list):

    number = int(input('Enter a number: '))
    less_than =[]

    for num in a:
        if num < number:
            less_than.append(num)
            return less_than
        else:
            print(f'We have no number less than {number}')
            
a = [ 2, 3, 5, 8, 13, 21, 34, 55, 89,1,1]
print(get_number(a))