słowa = []
with open("pary.txt") as plik:
    for wiersz in plik:
        słowa.append(wiersz.strip().split()[1])
print(słowa)

for słowo in słowa:
    długość = długość_ostateczna= 0
    wycinek = wycinek_ostateczny = ""
    for i in range(len(słowo)):
        if i == 0:
            długość = 1
            wycinek = słowo[i]
        elif słowo[i] == słowo[i-1]:
            długość += 1
            wycinek += słowo[i]
        else:
            długość_ostateczna = max(długość_ostateczna, długość)
            if len(wycinek_ostateczny) < len(wycinek):
                wycinek_ostateczny = wycinek
            długość = 1
            wycinek = słowo[i]
    print(wycinek_ostateczny, długość_ostateczna)
