from math import gcd

lista = []
file = open("/home/bartek/Documents/Matura/24-05-zalaczniki/Dane/skrot2.txt")
for verse in file:
    lista.append(int(verse.strip()))
file.close()

def skrot(n):
    m = 0
    y = 1
    while n > 0:
        if not n % 2 == 0:
            m = m + n % 10 * y
            y *= 10
        else:
            pass
        n = n // 10
    return m

for number in lista:
    if gcd(number, skrot(number)) == 7:
        print(number)

        