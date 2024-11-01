wiersze1 = []
with open("instrukcje.txt") as plik:
    for wiersz in plik:
        wiersze1.append(wiersz.strip().split())
#zad 4.1
długość_wyrazu = 0
for wiersz in wiersze1:
    if wiersz[0] == "DOPISZ":
        długość_wyrazu +=1
    elif wiersz[0] == "USUN":
        długość_wyrazu -= 1
print(długość_wyrazu)

#zad 4.2, 4.3
wiersze1sze = [] #lista samych komend
for wiersz in wiersze1:
    wiersze1sze.append(wiersz[0])

def długość(wiersze):
    długość_kolejnych = 1
    długość_max = 0
    instrukcja = ""
    for n in range(1, len(wiersze)):
        if n == len(wiersze) - 1 and wiersze[n] == wiersze[n-1]:
                długość_kolejnych += 1
                if długość_max < długość_kolejnych:
                    instrukcja = wiersze[n]
                długość_max = max(długość_max, długość_kolejnych)
        elif wiersze[n] != wiersze[n-1]:
            if długość_max < długość_kolejnych:
                instrukcja = wiersze[n-1]
            długość_max = max(długość_max, długość_kolejnych)
            długość_kolejnych = 1
        elif wiersze[n] == wiersze[n - 1]:
            długość_kolejnych += 1
    return instrukcja, długość_max

wiersze_dopisz = [] # lista liter po komendzie "DOPISZ", posortowana
for wiersz in wiersze1:
    if wiersz[0] == "DOPISZ":
        wiersze_dopisz.append(wiersz[1])
wiersze_dopisz = sorted(wiersze_dopisz)

print(długość(wiersze1sze))
print(długość(wiersze_dopisz))

#zad 4.4
alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V", "W","X","Y","Z"]
napis = ""

for wiersz in wiersze1:
    komenda, litera = wiersz
    if komenda == "DOPISZ":
        napis += litera
    elif komenda == "ZMIEN":
        napis = napis[:-1] + litera
    elif komenda == "USUN":
        napis = napis[:-1]
    elif komenda == "PRZESUN":
        if litera == "Z":
            napis = napis.replace(litera, "A", 1)
        else:
            index = alfabet.index(litera)
            napis = napis.replace(litera,alfabet[index + 1], 1)
print(napis)