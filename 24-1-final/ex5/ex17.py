f = open("words.txt", "r")
count = 0
for line in f:
    word = line.strip()
    if not "e" in word:
        count += 1
print(count)
f.close()