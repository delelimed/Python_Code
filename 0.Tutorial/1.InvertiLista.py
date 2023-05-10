'''
Scriviammo un programma che:
- chiede di quanti elementi è composta una lista;
- chiede gli elementi della lista;
- inverte la lista
'''

#prenti il numero di elementi
elem_lista = int(input("Di quanti elementi è composta la lista? "))

#chiedo gli elementi della lista
Lista = []
for h in range(elem_lista):
    elemento = str(input("Dimmi un solo elemento: "))
    Lista.append(elemento)

#Lista = Lista[::-1]
Lista.reverse()

print(Lista)
