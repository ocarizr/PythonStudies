if 2 == 2 and 3 > 1:
    print('chegou aqui')

a = 10
b = 12
c = 15

if a > b:
    print('primeiro')
elif a > c:
    print('segundo')
else:
    print('terceiro')

l = [6,4,5,6,7,8,9,9,10,5]

for var in l:
    if var >= 7:
        print('Aprovado')
    elif var >= 5:
        print('Exame')
    else:
        print('Reprovado')


sum_ = 0
i = 0
for var in l:
    sum_ += var
    i += 1

avg = sum_ / i
print(avg)

s = sum(l)

print(s)
print(sum_)

teste = True
i = 0

while teste:
    i += 1
    print(i)
    if i == 20:
        teste = False

x = 1
lista = []

while True:
    lista.append(x)
    x += 1

    if x > 10:
        break

print(lista)
print(lista[::2])

r = range(0, 31, 3)
print(type(r))

lst = list(r)

print(lst)

for var in range(0, 16):
    print(var)

novaLista = []

for var in range(1, 31):
    novaLista.append(var)

print(novaLista)

maisNovaLista = [var for var in range(1,21)]
print(maisNovaLista)

testelista = [var for var in range(1, 51) if var % 2 == 0]
print(testelista)

#Conversão de temperaturas de Celsius para Fahrenheit
celsius = [0, 10, 15, 20, 30, 50, 100]

fahrenheit = [ (temp * (9/5) + 32) for temp in celsius]

print(celsius)
print(fahrenheit)


l = [var for var in range(1,21) if var % 2 == 0]
i = 0

while i < len(l):
    print(l[i])
    i += 1
