import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("input a num: "))
if is_prime(number):
    print(number, "is prime")
else:
    print(number, "is not prime")