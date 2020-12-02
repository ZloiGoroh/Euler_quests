import math
limit_number = 2000000

def number_is_simple(number):       # If number is simple, returns true, otherwise false
    for n in range(2, int(math.sqrt(number) + 1)):
        if number % n == 0:
            return False
    return True

if __name__ == '__main__':
    print(number_is_simple(10000))
    sum = 0
    for iterable in range(2, limit_number):
        if number_is_simple(iterable):
            sum += iterable
    print(sum)
