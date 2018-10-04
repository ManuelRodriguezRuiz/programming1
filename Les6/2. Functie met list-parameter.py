def som(getallenlijst):
    antwoord = 0
    for x in getallenlijst:
        antwoord = antwoord + x
    return antwoord

print(som([3, 2, 4]))
