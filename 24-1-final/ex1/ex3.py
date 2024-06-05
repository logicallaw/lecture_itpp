medals = [('Australia', 0, 2, 1),
          ('Austria', 5, 3, 6),
          ('Belarus', 2, 1, 0),
          ('Belgium', 0, 1, 0),
          ('China', 1, 6, 2),
          ('Czech Republic', 2, 2, 3),
          ('Finland', 1, 1, 4),
          ('France', 5, 4, 6),
          ('Germany', 14, 10, 7),
          ('Hungary', 1, 0, 0),
          ('Italy', 3, 2, 5),
          ('Japan', 4, 5, 4),
          ('Netherlands', 8, 6, 6),
          ('New Zealand', 0, 0, 2),
          ('Norway', 14, 14, 11),
          ('Poland', 1, 0, 1),
          ('Russia', 2, 6, 9),
          ('Slovakia', 1, 2, 0),
          ('Slovenia', 0, 1, 1),
          ('South Korea', 5, 8, 4),
          ('Sweden', 7, 6, 1),
          ('Switzerland', 5, 6, 4),
          ('Ukraine', 1, 0, 0),
          ('United States', 9, 8, 6)]

def print_totals1(medals):
    for country, g, s, b in medals:
        print(country, ":", g + s + b)

def print_totals2(medals):
    for item in medals:
        print(item[0] + ":", sum(item[1:]))

print_totals1(medals)
print("---")
print_totals2(medals)