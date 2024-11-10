def wczytaj_dane(nazwa_pliku):
    with open(nazwa_pliku) as plik:
        return [wiersz.strip() for wiersz in plik]

def zapisz_do_pliku(nazwa_pliku, dane):
    with open(nazwa_pliku, "w") as plik:
        plik.write(dane)

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
#print(zapisz_do_pliku("zad_4.2", zad_4_2(wczytaj_dane("slowa_przyklad.txt"))))

if __name__ == "__main__":
    dane = wczytaj_dane("slowa.txt")
    dane_zad_4_2 = " ".join(zad_4_2(dane))
    zapisz_do_pliku("zad_4.2", dane_zad_4_2)