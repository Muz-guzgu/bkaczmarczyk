wiersze = []
with open("pary.txt") as plik:
    for wiersz in plik:
        wiersze.append(wiersz.strip().split())

wiersze_równe = []
for wiersz in wiersze:
    if int(wiersz[0]) == len(wiersz[1]):
        wiersze_równe.append(wiersz)

def która_mniejsza(wiersz1, wiersz2):
    if int(wiersz1[0]) > int(wiersz2[0]):
        return wiersz2
    elif int(wiersz1[0]) < int(wiersz2[0]):
        return wiersz1
    elif wiersz1[1] > wiersz2[1]:
        return wiersz2
    elif wiersz1[1] < wiersz2[1]:
        return wiersz1
    else:
        return wiersz1

wiersz_min = wiersze_równe[0]

for wiersz in wiersze_równe:
    wiersz_min = która_mniejsza(wiersz_min, wiersz)
print(wiersz_min)