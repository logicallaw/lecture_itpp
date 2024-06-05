def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def concatenate_strings(*args):
    result = ""
    for string in args:
        result += string
    return result

print(concatenate_strings("junho", "hi", 2))