def odczytaj_plik(plik):
    with open(plik) as plik:
        return [wiersz.strip() for wiersz in plik]

def zad_4_1(dane):
    wynik = [wiersz[9] for index, wiersz in enumerate(dane) if (index + 1) % 40 == 0 ]
    return "".join(wynik)

def zad_4_2(dane):
    lista_wierszy = []
    for wiersz in dane:
        wiersz_lista = {litera for litera in wiersz}
        lista_wierszy.append(wiersz_lista)
    slowo_set = max(slowo for slowo in lista_wierszy)
    slowo = dane[lista_wierszy.index(slowo_set)]
    return slowo, str(len(slowo_set))

def zad_4_3(dane):
    dane_max_10 = []
    for wiersz in dane:
        czy_max_10 = True
        for litera1 in wiersz:
            for litera2 in wiersz:
                if not -10 <= ord(litera1) - ord(litera2) <= 10:
                    czy_max_10 = False
                    break
            if czy_max_10 == False:
                break
        if czy_max_10 == True:
            dane_max_10.append(wiersz)
    return dane_max_10


def zapisz_plik(nazwa_pliku, dane):
    with open(nazwa_pliku, "w") as plik:
        plik.write(dane)


if __name__ == "__main__":
    dane = odczytaj_plik("sygnaly.txt")
    dane_zad_4_1 = zad_4_1(dane)
    dane_zad_4_2 = " ".join(zad_4_2(dane))
    dane_zad_4_3 = " ".join(zad_4_3(dane))
    dane_wszystkich = f"4.1 {dane_zad_4_1}\n4.2 {dane_zad_4_2}\n4.3 {dane_zad_4_3}"
    zapisz_plik("wyniki4.txt", dane_wszystkich)
