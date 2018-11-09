maand = eval(input('Geef de maand: '))
def seizoen(maand):
    maanden_winter = 12, 1, 2
    maanden_lente = 3, 4, 5
    maanden_zomer = 6, 7, 8
    maanden_herfst = 9, 10, 11
    if maand in maanden_winter:
        return "Het is winter!"
    elif maand in maanden_lente:
        return "Het is lente!"
    elif maand in maanden_zomer:
        return "Het is zomer!"
    elif maand in maanden_herfst:
        return "Het is Herfst!"
    else:
        return "Deze maand bestaat helaas niet."

print(seizoen(maand))
print(seizoen(1))
print(seizoen(3))
print(seizoen(6))
print(seizoen(11))
print(seizoen(13))
