f = open("words.txt", "r")
for line in f:
    word = line.strip()
    if 'a' in word.lower():
        if word.lower().count('a') >= 5:
            print(word)
f.close()