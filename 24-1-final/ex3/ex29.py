def is_abecedarian(word):
    for i in range(1, len(word)):
        if word[i - 1].lower() > word[i].lower():
            return False
    return True

f = open("../words.txt", "r")
for line in f:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
