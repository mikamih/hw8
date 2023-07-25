import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def expression_value(n):
    result = 0
    for i in range(1, n+1):
        result += factorial(i)
    return result

n = int(input("input number: "))

value = expression_value(n)

print("result: ", value)