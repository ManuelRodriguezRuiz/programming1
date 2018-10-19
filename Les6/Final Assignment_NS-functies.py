def standaardtarief(afstandKM):
    if afstandKM > 50:
        standaardprijs = (afstandKM * 0.6) + 15
    elif afstandKM < 0:
        afstandKM = 0
        standaardprijs = 0
    else:
        standaardprijs = afstandKM * 0.8
    return standaardprijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    weekendrit = weekendrit.lower()
    standaardprijs = standaardtarief(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        prijs = standaardprijs * 0.7
    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == "ja":
        prijs = (standaardprijs * 0.7) * 0.65
    elif weekendrit == "ja":
        prijs = standaardprijs * 0.6
    else:
        prijs = standaardprijs
    return prijs

print(ritprijs(11, "ja", 49))
print(ritprijs(11, "ja", 51))
print(ritprijs(11, "nee", 49))
print(ritprijs(11, "nee", 51))
print(ritprijs(11, "nee", -10))
print(ritprijs(11, "ja", -10))
print(ritprijs(12, "ja", 49))
print(ritprijs(12, "ja", 51))
print(ritprijs(12, "nee", 49))
print(ritprijs(12, "nee", 51))
print(ritprijs(12, "nee", -10))
print(ritprijs(12, "ja", -10))
print(ritprijs(64, "ja", 49))
print(ritprijs(64, "ja", 51))
print(ritprijs(64, "nee", 49))
print(ritprijs(64, "nee", 51))
print(ritprijs(64, "nee", -10))
print(ritprijs(64, "ja", -10))
print(ritprijs(65, "ja", 49))
print(ritprijs(65, "ja", 51))
print(ritprijs(65, "nee", 49))
print(ritprijs(65, "nee", 51))
print(ritprijs(65, "nee", -10))
print(ritprijs(65, "ja", -10))