f = open("planets.txt", "r")
current = 0
earth = 0
for line in f:
    current += 1
    planet = line.strip().lower()
    if planet == "earth":
        earth = current
        break
print("Earth is planet #%d." %earth)

f.close()