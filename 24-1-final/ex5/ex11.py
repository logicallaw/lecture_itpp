f = open("planets.txt", "r")
planets = []
for line in f:
    planets.append(line.strip())
print(planets)
f.close()