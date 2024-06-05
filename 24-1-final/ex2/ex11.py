def print_kwargs(**kwargs):
    print(kwargs)
    return kwargs

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")