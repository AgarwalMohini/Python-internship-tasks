#To check if a number is prime or not

from math import isqrt

def is_prime(n):
    if n <= 1:
        return False  
    if n <= 3:
        return True  
    if n % 2 == 0 or n % 3 == 0:
        return False  
    for i in range(5, isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

n = int(input("Enter an integer: "))
print(is_prime(n))
