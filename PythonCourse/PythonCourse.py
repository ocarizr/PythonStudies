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