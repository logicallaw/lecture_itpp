def student(name, mscore, fscore, ascore):
    f = open("student.txt", "a")
    avg = (mscore + fscore + ascore) / 3
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    else:
        grade = "C"
    text = "%s|%d|%d|%d|%.2f|%s\n" %(name, mscore, fscore, ascore, avg, grade)
    f.write(text)
    f.close()

# student("Jerry", 90, 89, 99)
# student("Eric", 56, 45, 80)
# student("Sun", 20, 79, 60)
# student("Jacob", 40, 39, 98)

def search(name):
    f = open("student.txt", "r")
    is_name = False
    for line in f:
        word = line.strip()
        if name in word:
            word_list = word.split("|")
            print("average:%s,grade:%s\n" %(word_list[4], word_list[5]))
            is_name = True
    if not is_name:
        print("없음\n")
    f.close()
    return

search("Sun")
search("Jacob")
search("Yuna")

