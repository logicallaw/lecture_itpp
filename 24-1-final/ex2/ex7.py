def add_numbers(*args):
    result = 0
    for number in args:
        result += number
    return result

print(add_numbers(1,2,3))