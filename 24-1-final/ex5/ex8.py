f = open("text1.txt", "a")
for i in range(11, 21):
    data = "This is line %d.\n" % i
    f.write(data)
f.close()