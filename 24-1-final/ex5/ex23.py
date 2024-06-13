def no_medals(countries, al, bl):
    result = []
    for i in range(len(countries)):
        if al[i] == 0 and bl[i] == 0:
            result.append(countries[i])
    return result

def top_10(countries, gold, silver, bronze):
    table = []
    for i in range(len(countries)):
        table.append((gold[i], silver[i], bronze[i], countries[i]))
    table.sort()
    top_ten = table[-10:]
    top_ten.reverse()
    return top_ten