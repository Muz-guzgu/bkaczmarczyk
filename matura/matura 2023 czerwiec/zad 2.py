def czy_mniejszy(n, s ,k1, k2):
    i = k1 - 1
    j = k2 - 1
    n = n - 1
    while i <= n and j <=n:
        if s[i] == s[j]:
            i = i + 1
            j = j + 1
        else:
            if s[i] < s[j]:
                return "TAK"
            else:
                return "NIE"
    if j <= n:
        return "TAK"
    else:
        return "NIE"

def wczytaj_plik(plik):
    with open(plik) as plik:
        return [wiersz.strip() for wiersz in plik]


def zad_2_3(slowo):
    len_slowo = len(slowo)
    T = [i for i in range(1, len_slowo + 1)]
    lista_indeksow = [i for i in range(1, len_slowo + 1)]
    for i in lista_indeksow:
        licznik = 0
        for j in lista_indeksow:
            if i != j and czy_mniejszy(len_slowo, slowo, i, j) == "NIE":
                licznik += 1
        T[licznik] = i
    return T

def najmnniejszy_sufiks(slowo):
    len_slowo = len(slowo)
    T = [i for i in range(1, len_slowo + 1)]
    lista_indeksow = [i for i in range(1, len_slowo + 1)]
    for i in lista_indeksow:
        licznik = 0
        for j in lista_indeksow:
            if i != j and czy_mniejszy(len_slowo, slowo, i, j) == "NIE":
                licznik += 1
        if licznik == 0:
            return slowo[i-1:]


def zapisz_plik(nazwa, dane):
    with open(nazwa, "w") as plik:
        plik.write(dane)


if __name__ == "__main__":
    dane_lista = [wczytaj_plik(f"slowa{i}.txt")for i in range(1,4)]
    wyniki_2_2 = [czy_mniejszy(int(dane[0]), dane[1], int(dane[2].split()[0]), int(dane[2].split()[1])) for dane in dane_lista]
    dane_2_4 = wczytaj_plik("slowa4.txt")
    wyniki_2_4 = [najmnniejszy_sufiks(wiersz.split()[1]) for wiersz in dane_2_4]
    wyniki_2_2_do_zapisu = f"slowa1.txt {wyniki_2_2[0]}\nslowa2.txt {wyniki_2_2[1]}\nslowa3.txt {wyniki_2_2[2]}"
    zapisz_plik("wyniki2_2", wyniki_2_2_do_zapisu)
    wyniki_2_4_do_zapisu = "\n".join([wiersz for wiersz in wyniki_2_4])
    zapisz_plik("wyniki2_4.txt", wyniki_2_4_do_zapisu)
    print(wyniki_2_4_do_zapisu)