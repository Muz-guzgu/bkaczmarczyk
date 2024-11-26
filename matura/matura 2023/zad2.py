def wczytaj_plik(plik):
    with open(plik) as plik:
        binarne = [wiersz.strip() for wiersz in plik]
    liczby = [int(str(wiersz), 2) for wiersz in binarne]
    return binarne, liczby


def zad_2_1(n): #ile blokow, tego nie wiedzialem jak
    ostatnia_binarna = n % 2
    b = 1
    n //= 2
    while n > 0:
        if ostatnia_binarna != n % 2:
            b += 1
        ostatnia_binarna = n % 2
        n //= 2
    return b


def zad_2_2(dane_liczby):
    return sum([1 for wiersz in dane_liczby if zad_2_1(wiersz) <= 2])


def zad_2_3(dane):
    dane = [int(wiersz) for wiersz in dane]
    return sorted(dane)[-1]


def zad_2_5(dane_binarne, dane_liczby):
    lista_pdiv2 = [bin(wiersz // 2)[2:] for wiersz in dane_liczby]

    lista_xor = []
    for i, p in enumerate(dane_binarne):
        pdiv2 = lista_pdiv2[i]
        xor = ""
        if len(p) != len(pdiv2):
            pdiv2 = ["0" + pdiv2 for i in range(len(p) - len(pdiv2))]
            pdiv2 = pdiv2[0]
        for j, litera_p in enumerate(p):
            litera_pdiv2 = pdiv2[j]
            if litera_p == litera_pdiv2:
                xor += "0"
            else:
                xor += "1"
        lista_xor.append(xor)
    return lista_xor


def zapisz_plik(nazwa, dane):
    with open(nazwa, "w") as plik:
        plik.write(dane)


if __name__ == "__main__":
    dane_liczby = wczytaj_plik("bin.txt")[1]
    dane_binarne = wczytaj_plik("bin.txt")[0]
    dane_zad_2_2 = zad_2_2(dane_liczby)
    dane_zad_2_3 = zad_2_3(dane_binarne)
    dane_zad_2_5 = "\n".join(zad_2_5(dane_binarne, dane_liczby))
    dane_wszystkich = f"2.2 {dane_zad_2_2}\n2.3 {dane_zad_2_3}"
    zapisz_plik("wyniki2.txt", dane_wszystkich)
    zapisz_plik("wyniki2_5.txt", dane_zad_2_5)