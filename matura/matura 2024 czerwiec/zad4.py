def wczytaj_dane(nazwa_pliku):
    with open(nazwa_pliku) as plik:
        return [wiersz.strip() for wiersz in plik]

def zapisz_dane(nazwa_pliku, dane):
    with open(nazwa_pliku, "w") as plik:
        plik.write(dane)

def zad_4_1(wiersze):
    licznik = 0
    for wiersz in wiersze:
        p = 0
        while p + 2 < len(wiersz):
            if wiersz[p] == "k" and wiersz[p+2] == "t":
                licznik += 1
                break
            p += 1
    return licznik

def zad_4_2(wiersze):
    lista_fragmentow = []
    for wiersz in wiersze:
        p = 0
        k = 5
        while k <= len(wiersz):
            fragment = wiersz[p:k]
            if fragment[0] == "e" and fragment[-1] == "e":
                lista_fragmentow.append(fragment)
            p += 1
            k += 1
    return lista_fragmentow


def zad_4_3(wiersze):
    najdluzszy = ""
    licznik = 0
    for wiersz in wiersze:
        if wiersz[::-1] == rot(wiersz):
            licznik += 1
            if len(wiersz) > len(najdluzszy):
                najdluzszy = wiersz
    return str(licznik) + " " + najdluzszy
def rot(wiersz):
    slowo = ""
    for litera in wiersz:
        ascii_litery = ord(litera)
        if ascii_litery < 110:
            ascii_litery += 13
        else:
            ascii_litery -= 13
        slowo = slowo + chr(ascii_litery)
    return slowo


def zad_4_4(wiersze):
    lista_slow = []
    for wiersz in wiersze:
        wiersz_sorted = "".join(sorted(wiersz))
        if licznik_największej(wiersz_sorted) >= len(wiersz)/2:
            lista_slow.append(wiersz)
    return lista_slow

def licznik_największej(slowo):
    licznik = 0
    max_licznik = 0
    for index in range(len(slowo)):
        if index == 0:
            licznik += 1
        if slowo[index] == slowo[index - 1]:
            licznik += 1
        else:
            licznik = 1
        max_licznik = max(licznik, max_licznik)
    return max_licznik


if __name__ == "__main__":
    dane = wczytaj_dane("slowa.txt")
    dane_zad_4_2 = " ".join(zad_4_2(dane))
    dane_zad_4_1 = zad_4_1(dane)
    dane_zad_4_3 = zad_4_3(dane)
    dane_zad_4_4 = " ".join(zad_4_4(dane))
    print(dane_zad_4_4)
    dane_do_zapisu = f"4.1 {dane_zad_4_1}\n4.2 {dane_zad_4_2}\n4.3 {dane_zad_4_3}\n4.4 {dane_zad_4_4}"
    zapisz_dane("zad_4", dane_do_zapisu)

