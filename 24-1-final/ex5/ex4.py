f = open("text1.txt", "w")
for i in range(1, 11):
    data = ("This is line %d.\n" %i)
    f.write(data)