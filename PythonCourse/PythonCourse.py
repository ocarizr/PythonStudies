def primeira_funcao():
    print("Teste")

primeira_funcao()

def retorna_tamanho(conjunto):
    i = 0
    for num in conjunto:
        i += 1
    return i

l = [1,2,3,4,5,6,7,8]

print(retorna_tamanho(l))

def eh_primo(valor):
    for num in range(2, valor):
        if valor % num == 0:
            return False
        return True

if eh_primo(67):
    print("Primo")
else:
    print("Nao_Primo")

def quadrado(num):
    return num * num

print(quadrado(8))

square = lambda num: num * num

print(square(3))

primeiro_char = lambda s: s[0]

print(primeiro_char("Rafael"))

file = open("test.txt", "w+")

lines = []

lines.append("Rafael Ocariz")
lines.append("Ricardo Zaviasky")
lines.append("Alex Kubo")
lines.append("Rafael Borgetti")
lines.append("Ziad Junior")
lines.append("Leandro Pessini")
lines.append("Lucas Nogueira")
lines.append("Daniel Gil Mendes")

for name in lines:
    file.write(name)

file.seek(0)

print(file.readline())