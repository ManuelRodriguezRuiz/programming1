bestand= open("Kaartnummers.txt")

test = bestand.read().splitlines()

for line in test:
    line = line.split(',')
    print(line[1], 'heeft kaartnummer:', line[0])