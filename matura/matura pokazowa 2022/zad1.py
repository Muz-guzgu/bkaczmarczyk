def wczytaj_dane(plik):
    with open(plik) as plik:
        return [wiersz.strip() for wiersz in plik]
def lista_plansz(dane):
    lista_plansz = []
    plansza = []
    for i, wiersz in enumerate(dane):
        if i == len(dane) - 1:
            plansza.append(wiersz)
            lista_plansz.append(plansza)
        elif wiersz:
            plansza.append(wiersz)
        else:
            lista_plansz.append(plansza)
            plansza = []
    return lista_plansz
def ile_pustych_wierszy(dane): #niepotrzebne jak cos
    max_pustych = 0
    for plansza in dane:
        puste_w_planszy = plansza.count("........")
        max_pustych = max(puste_w_planszy, max_pustych)
    return sum([1 for plansza in dane if "........" in plansza]), max_pustych


def ile_pustych_kolumn(dane):
    max_kolumn = 0
    plansze_z_pustymi = 0
    for plansza in dane:
        puste_kolumny = 0
        for kolumna in range(8):
            czy_pusta = True
            for wiersz in range(8):
                if plansza[wiersz][kolumna] != ".":
                    czy_pusta = False
                    break
            if czy_pusta == True:
                puste_kolumny += 1
        max_kolumn = max(puste_kolumny, max_kolumn)
        if puste_kolumny > 0:
            plansze_z_pustymi += 1
    return plansze_z_pustymi, max_kolumn



if __name__ == "__main__":
    dane = wczytaj_dane("szachy_przyklad.txt")
    plansze = lista_plansz(dane)
    print(plansze)
    print(ile_pustych_kolumn(plansze))