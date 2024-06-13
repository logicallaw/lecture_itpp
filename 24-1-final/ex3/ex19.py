def add_student(grades, name, score):
    grades[name] = score

def get_score(grades, name):
    return grades[name]

def remove_student(grades, name):
    del grades[name]

def print_all_students(grades):
    for key, value in grades.items():
        print("{0} : {1}".format(key, value))

grades = dict()
add_student(grades, "Alice", 85)
add_student(grades, "Bob", 92)

score = get_score(grades, "Alice")
print(f"Alice's score: {score}")


print_all_students(grades)