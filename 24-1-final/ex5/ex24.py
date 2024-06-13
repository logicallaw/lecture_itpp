def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
print(add_many(1,2,3,4,5))

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for a in args:
            result += a
    elif choice == "mul":
        result = 1
        for a in args:
            result *= a
    return result

print(add_mul("mul", 1,2,3,4,5))