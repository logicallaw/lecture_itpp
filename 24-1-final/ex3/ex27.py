f = open("../words.txt", "r")
for line in f:
    word = line.strip()
    if len(word) > 10:
        print(word)

f.close()