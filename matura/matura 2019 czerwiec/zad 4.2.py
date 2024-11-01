liczby = []
with open("pierwsze.txt") as plik:
    for wiersz in plik:
        liczby.append(wiersz.strip())

def czy_pierwsza(n):
    dzielnik = 2
    while dzielnik <= n/2:
        if n % dzielnik == 0:
            return False
        else:
            dzielnik += 1
    return True

for wiersz in liczby:
    if czy_pierwsza(int(wiersz)) == True and czy_pierwsza(int(wiersz[::-1])) == True:
            print(wiersz)