count = 0
def has_double_letters(word):
    word_list = list(word)
    for i in range(0, len(word) - 1):
        if word_list[i] == word_list[i + 1]:
            count += 1
            return

f = open("words.txt", "r")
for line in f:
    word = line.strip()
    has_double_letters(word)

print(count)
f.close()
