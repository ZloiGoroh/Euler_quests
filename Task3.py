import math


def IsPrime(n):         #Checking if the number is prime
    d = 2               #returns true if it is prime and
    while n % d != 0:   #fals if it is not
        d += 1
    return d == n


a = 600851475143
print(a)
for i in range(3, math.ceil(math.sqrt(a))):
    if (a % i == 0) and (IsPrime(i)):
        b = i
print(b)
