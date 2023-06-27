import math

def findPrimeFactors(x):
    if isPrimeNumber(x):
        return [x]
    list = []
    y = 2
    while y <= x and x > 1:
        if x % y == 0 and isPrimeNumber(y):
            list.append(y)
            x = int(x / y)
        else:
            y += 1
    return list

def isPrimeNumber(x):
    for y in range(2, math.ceil(math.sqrt(x))):
        if x % y == 0:
            return False
    return True

print(findPrimeFactors(630)) #[2, 3, 5, 7]
print(findPrimeFactors(13)) #[13]