def char_frequency(s, char):
    return s.count(char)

def word_frequency(s):
    result = dict()
    for i in s:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


