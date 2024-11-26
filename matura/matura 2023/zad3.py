def wczytaj_plik(plik):
    with open(plik) as plik:
        return [wiersz.strip() for wiersz in plik]


def zad_3_1(dane):
    return sum([1 for i in range(len(dane)-1) if dane[i] == "9" and dane[i+1] != "0"])


def dane_fragmentow(dane):
    return [dane[i]+dane[i+1] for i in range(len(dane)-1)]


def zad_3_2(dane):
    najwieksza = ""
    najmniejsza = ""
    ilosc_najwiekszych = 0
    ilosc_najmniejszych = 10000
    for i in range(100):
        if i < 10:
            j = f"0{i}"
        else:
            j = str(i)
        liczba_fragmentow = dane.count(j)
        if liczba_fragmentow > ilosc_najwiekszych:
            najwieksza = j
            ilosc_najwiekszych = liczba_fragmentow
        if liczba_fragmentow < ilosc_najmniejszych:
            najmniejsza = j
            ilosc_najmniejszych = liczba_fragmentow
    return najmniejsza, ilosc_najmniejszych, najwieksza, ilosc_najwiekszych


if __name__ == "__main__":
    dane = wczytaj_plik("pi.txt")
    dane_zad_3_1 = zad_3_1(dane)
    dane_fragmentow = dane_fragmentow(dane)
    dane_zad_3_2 = zad_3_2(dane_fragmentow)
    print(dane_zad_3_2)