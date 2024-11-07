with open("liczby.txt") as plik:
    liczby = [wiersz.strip() for wiersz in plik]

#zad 4.1
lista_takie_same = [liczba
                    for liczba in liczby
                    if liczba[0] == liczba[-1]]
print(len(lista_takie_same), lista_takie_same[0])

#zad 4.2
def rozklad_na_czynniki(liczba):
    n = 2
    lista_czynnikow = []
    while liczba > 1:
        if liczba % n == 0:
            liczba = liczba / n
            lista_czynnikow.append(n)
        else:
            n += 1
    return lista_czynnikow

czynniki_pierwsze_liczb = [rozklad_na_czynniki(int(liczba)) for liczba in liczby]
len_max_czynnikow = 0
len_max_roznych_czynnikow = 0

for czynniki in czynniki_pierwsze_liczb:
    if len_max_czynnikow < len(czynniki):
        index_max_czynnikow = czynniki_pierwsze_liczb.index(czynniki)
        len_max_czynnikow = len(czynniki)
    czynniki_set = set(czynniki)
    if len_max_roznych_czynnikow < len(czynniki_set):
        index_roznych_czynnikow = czynniki_pierwsze_liczb.index(czynniki)
        len_max_roznych_czynnikow = len(czynniki_set)

print(liczby[index_max_czynnikow], len_max_czynnikow, liczby[index_roznych_czynnikow], len_max_roznych_czynnikow)

#zad 4.3
liczby_int = [int(liczba) for liczba in liczby]
liczby_sorted = sorted(liczby_int)
ilosc_trojek = 0
ilosc_piatek = 0
lista_trojek = []
for liczba_1 in liczby_sorted:
    for liczba_2 in liczby_sorted:
        if liczba_2 % liczba_1 == 0 and liczba_2 != liczba_1:
            for liczba_3 in liczby_sorted:
                if liczba_3 % liczba_2 == 0 and liczba_3 != liczba_2:
                    ilosc_trojek +=1
                    lista_trojek.append([liczba_1,liczba_2, liczba_3])
                    for liczba_4 in liczby_sorted:
                        if liczba_4 % liczba_3 == 0 and liczba_4 != liczba_3:
                            for liczba_5 in liczby_sorted:
                                if liczba_5 % liczba_4 == 0 and liczba_5 != liczba_4:
                                    ilosc_piatek += 1
print(ilosc_trojek, ilosc_piatek, lista_trojek)