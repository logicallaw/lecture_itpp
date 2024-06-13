def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1, b = 2)

def my_function(**kwargs):
    print("His last name is " + kwargs["lname"])

my_function(fname = "Tobias", lname = "j")

def add_and_mul(a, b):
    return a + b, a * b
print(add_and_mul(1,2)[1])