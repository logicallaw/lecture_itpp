f = open("../words.txt", "r")
for line in f:
    tmp = line.strip()
    word = tmp.lower()
    if 'a' in word:
        count = word.count('a')
        if count >= 5:
            print(tmp)

f.close()