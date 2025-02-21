lista = [1,2,3,4,5,6,7,7]
lista.append(7) 
count =lista.count(7)
lista.append(8)
lista.reverse()
print(lista)
print(count)
lista2 = [1,2,3]
lista2.clear()
lista3 = [1,2]

lista2.extend(lista3)
print(lista2)
index = lista2.index(2)
print(index)