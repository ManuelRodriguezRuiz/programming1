cijferICOR=6
cijferPROG=8
cijferCSN=7
cijfers = [cijferICOR, cijferPROG, cijferCSN]
som = sum(cijfers)
gemiddelde = som / len(cijfers)
beloning = som * 30
overzicht = 'Mijn cijfers (gemiddeld een' + str(gemiddelde) + ') leveren een beloning voor van € ' + str(beloning)
print(overzicht)
