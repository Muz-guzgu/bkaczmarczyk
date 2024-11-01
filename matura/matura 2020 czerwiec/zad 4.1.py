liczby = []
with open("pary.txt") as plik:
    for wiersz in plik:
        liczby.append(int(wiersz.split()[0]))

liczby_parzyste = []
for liczba in liczby:
    if liczba % 2 == 0:
        liczby_parzyste.append(liczba)

def czy_pierwsza(n):
    if n == 1:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True

for liczba in liczby_parzyste:
    for i in range(2, liczba):
        reszta = liczba - i
        if czy_pierwsza(i) == True and czy_pierwsza(reszta) == True:
            print(liczba, i, reszta)
            break
        else:
            continue