def print_info(**kargs):
    for key, value in kargs.items():
        print(f"{key} : {value}")

print_info(name = "Alice", age = 25, city = "Seoul")