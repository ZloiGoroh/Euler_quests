import math


def palindrome(n):              #Function turns number into a string
    n = str(n)                  #Than it check first and last symbol on equality
    for k in range(math.ceil(len(n)/2)):
        if n[k] != n[-k - 1]:
            return False
    return True


solution = 0
for i in range(100, 999):
    for j in range(100, 999):           #Simple iteration of multipliers
        multiple = i*j
        if multiple > solution and palindrome(multiple):
            solution = multiple
print(solution)
