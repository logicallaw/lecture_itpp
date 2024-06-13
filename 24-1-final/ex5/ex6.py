f = open("text1.txt", "r")
lines = f.readlines()
for line in lines:
    print(line, end= ' ')

f.close()