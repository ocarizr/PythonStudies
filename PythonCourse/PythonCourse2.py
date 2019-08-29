t = [1,2,3]

print(t)
print(type(t))

myfile = open('file.txt', 'w+')

myfile.write("teste")
myfile.seek(0)
print(myfile.readline())

x = set()
print(type(x))
x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(5)
x.add(1)
print(x)

b = True
print(type(b))

print(b)

n1 = 10
n2 = 2
n3 = 3
n4 = 4
n5 = (n1 + n4 - n3 * n2) / n2

print(n5)
print(type(n5))

n6 = 3 ** 2
print(n6)
n7 = n6 ** 0.5
print(n7)

s = "hello"
print(s[1])

print(s[4])
print(s[-1])
print(s[::2])

print(s[::-1])

lista = [1]
print(type(lista))
print(lista)
lista.append(2)
lista.append(3)
lista.append(4)
print(lista)

l2 = [1] * 3

print(l2)

l = [5,3,4,6,1]
print(l)
l.sort()
print(l)

d = {'Rafael':29,'Joao':30,'Maria':26,'Evelyn':25}
print(type(d))
print(d)
d['Andre'] = 35
print(d)
print(d.keys())
print(d.values())
lTwo = d.items()

print(type(lTwo))
print(lTwo)

l3 = [1,1,1,1,2,4,3,4,5,5,6,6,7]
l3.sort
s = set(l3)
print(s)
