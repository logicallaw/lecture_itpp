countries = ["Australia", "Austria", "Belarus", "Belgium", "Canada",
             "China", "Czech Republic", "Finland", "France", "Germany",
             "Great Britain", "Hungary", "Italy", "Japan", "Netherlands",
             "New Zealand", "Norway", "Poland", "Russia", "Slovakia",
             "Slovenia", "South Korea", "Sweden", "Switzerland", "Ukraine", "United States"]

gold = [0, 5, 2, 0, 11, 1, 2, 1, 5, 14, 1, 1, 3, 4, 8, 0, 14, 1, 2, 1, 0, 5, 7, 5, 1, 9]

silver = [2, 3, 1, 1, 8, 6, 2, 1, 4, 10, 0, 0, 2, 5, 6, 0, 14, 0, 6, 2, 1, 8, 6, 6, 0, 8]

bronze = [1, 6, 0, 0,10, 2, 3, 4, 6, 7, 4, 0, 5, 4, 6, 2, 11, 1, 9, 0, 1, 4, 1, 4, 0, 6]

totals = []
for i in range(len(countries)):
    medals = gold[i] + silver[i] + bronze[i]
    totals.append((medals, countries[i]))

print(totals)