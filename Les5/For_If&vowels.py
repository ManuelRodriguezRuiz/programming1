s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = 'iouae'
for char in s:
    if char in klinkers:
        print(char)