liczby = []
with open("pierwsze.txt") as plik:
    for wiersz in plik:
        liczby.append(int(wiersz))

def waga_liczby(liczba):
    while liczba >= 10:
        waga = 0
        for litera in str(liczba):
            cyfra = int(litera)
            waga += cyfra
        liczba = waga
    return waga

ile_liczb = 0

for wiersz in liczby:
    if waga_liczby(wiersz) == 1:
        ile_liczb +=1
print(ile_liczb)