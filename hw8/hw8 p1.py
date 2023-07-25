def is_int(num):
    if num.is_integer():
        return True
    else:
        return False

num = float(input("input a number: "))

if is_int(num):
    print(f'{int(num)} is an interger')
else:
    print(f'{num} is not an in terger')