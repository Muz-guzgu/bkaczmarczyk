lista_pierwsze = []
lista_całkowite = []
plik = open("liczby.txt")
wiersze = plik.readlines()
plik.close()
lista_pierwsze_string = wiersze[0].strip().split()
lista_całkowite_string = wiersze[1].strip().split()

for i in lista_pierwsze_string:
    lista_pierwsze.append(int(i))
for j in lista_całkowite_string:
    lista_całkowite.append(int(j))
#zad 4.1.py.py
x = 0

for liczba in lista_pierwsze:
    for liczba2 in lista_całkowite:
        if liczba2 % liczba == 0:
            x += 1
            break
print(x)

#zad 4.2
lista_pierwsze_sorted = sorted(lista_pierwsze)
lista_pierwsze_sorted.reverse()
print(lista_pierwsze_sorted[100])

#zad 4.3.
for całkowita in lista_całkowite:
    całkowita_dzielona = całkowita
    for pierwsza in lista_pierwsze:
        if całkowita_dzielona % pierwsza == 0:
            całkowita_dzielona = całkowita_dzielona / pierwsza
    if całkowita_dzielona == 1:
        print(całkowita)
