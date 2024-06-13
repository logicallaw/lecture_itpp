def add_book(library, title, author):
    library[title] = author

def get_author(library, title):
    return library[title]

def remove_book(library, title):
    del library[title]

def print_all_books(library):
    for key, value in library.items():
        print("{0} : {1}".format(key, value))

library = {}
add_book(library, "Harry Potter", "J.K. Rowling")
add_book(library, "To Kill a Mockingbird", "Harper Lee")

author = get_author(library, "Harry Potter")
print(f"The author of 'Harry Potter' is {author}")

remove_book(library, "To Kill a Mockingbird")

print_all_books(library)
