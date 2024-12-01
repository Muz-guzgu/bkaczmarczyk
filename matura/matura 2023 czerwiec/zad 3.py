
def wczytaj_plik(plik):
    with open(plik) as plik:
        return [wiersz.strip() for wiersz in plik]


def zad_3_1(dane):
    zrownowazone = sum([1 for wiersz in dane if wiersz.count("0") == wiersz.count("1")])
    prawie_zrownowazone = sum([1 for wiersz in dane
                               if wiersz.count("0") == wiersz.count("1") - 1 or wiersz.count("0") == wiersz.count("1") + 1])
    return f"{zrownowazone}\n{prawie_zrownowazone}"


def zad_3_2(dane):
    liczba_kombinacji_max = 0
    lista_wierszy = []
    for wiersz in dane:
        if len(wiersz) == 8:
            liczba_zer = wiersz.count("0")
            liczba_jedynek = wiersz.count("1")
            liczba_kombinacji = min(liczba_zer, liczba_jedynek - 1)
            if liczba_kombinacji > liczba_kombinacji_max:
                liczba_kombinacji_max = liczba_kombinacji
                lista_wierszy = [wiersz]
            elif liczba_kombinacji == liczba_kombinacji_max:
                lista_wierszy.append(wiersz)
    return "\n".join(lista_wierszy)


def zad_3_3(dane):
    max_roznica = 0
    for i in range(len(dane)-1):
        roznica = abs(dane[i] - dane[i+1])
        max_roznica = max(max_roznica, roznica)
    return bin(max_roznica)[2:]


def zad_3_4(dane):
    dane_str = [str(wiersz) for wiersz in dane]
    suma_bez_zera = sum([1 for wiersz in dane_str if not "0" in wiersz])
    lista_dane = []
    lista_int = []
    suma_roznych_max = 0
    for wiersz in dane_str:
        lista_dane.append([litera for litera in wiersz])
    for wiersz in lista_dane:
        lista_int.append([int(litera) for litera in wiersz])
    for wiersz in lista_int:
        suma_roznych = sum(set(wiersz))
        if suma_roznych > suma_roznych_max:
            suma_roznych_max = suma_roznych
            liczba_z_najwieksza_suma = dane[lista_int.index(wiersz)]
    return f"{suma_bez_zera}\n{liczba_z_najwieksza_suma}"


def zapisz_plik(nazwa, dane):
    with open(nazwa, "w") as plik:
        plik.write(dane)


if __name__ == "__main__":
    dane = wczytaj_plik("anagram.txt")
    dane_dziesietne = [int(wiersz, 2) for wiersz in dane]
    dane_3_1 = zad_3_1(dane)
    dane_3_2 = zad_3_2(dane)
    dane_3_3 = zad_3_3(dane_dziesietne)
    dane_3_4 = zad_3_4(dane_dziesietne)
    dane_do_zapisu = f"3.1\n{dane_3_1}\n3.2\n{dane_3_2}\n3.3\n{dane_3_3}\n3.4\n{dane_3_4}"
    zapisz_plik("wyniki3.txt", dane_do_zapisu)