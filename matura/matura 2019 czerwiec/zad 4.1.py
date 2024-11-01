liczby = []
with open("liczby.txt") as plik:
    for wiersze in plik:
        liczby.append(int(wiersze))

def czy_pierwsza(n):
    pierwsza = True
    dzielnik = 2
    while dzielnik <= n/2:
        if n % dzielnik == 0:
            pierwsza = False
            return pierwsza
        else:
            dzielnik +=1
    return pierwsza

for wiersz in liczby:
    if czy_pierwsza(wiersz) == True and 100 <= wiersz <= 5000:
        print(wiersz)