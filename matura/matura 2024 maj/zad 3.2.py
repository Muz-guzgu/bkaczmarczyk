lista = []
file = open("/home/bartek/Documents/Matura/24-05-zalaczniki/Dane/skrot.txt")
for verse in file:
    lista.append(int(verse.strip()))
file.close()

def m(n):
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

odd_amount = 0
max_nr = 0
for number in lista:
    odd = m(number)
    if odd == 0:
        odd_amount +=1
        max_nr = max(max_nr, number)
print(odd_amount, max_nr)