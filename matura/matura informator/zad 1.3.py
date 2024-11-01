lines = []
file = open("dane1_3.txt")
for i in file:
    lines.append(i.strip())
    file.close()
'''plik = open('dane1_3.txt', 'r')
lista = plik.readlines()
plik.close()

lista_new = [int(i.rstrip('\n')) for i in lista]
print(lista_new)'''
n = -100
for line in lines:
    if int(line) > int(n):
        n = line
    else:
        continue
print(n)