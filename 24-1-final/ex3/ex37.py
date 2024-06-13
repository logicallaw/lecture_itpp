def no_medals(countries, al, bl):
    result = []
    for i in range(len(countries)):
        if al[i] == 0 and bl[i] == 0:
            result.append(countries[i])
    return result
