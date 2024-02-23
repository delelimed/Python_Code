numero_elementi= int(input("Quanti elementi ha la lista? "))

Lista = []
for h in range(numero_elementi):
    elemento=str(input("inserire un elemento "))
    Lista.append(elemento)

passi_swap = int(input("Di quanti passi eseguo lo swap? "))

for figa in range(passi_swap):
    Lista.append(Lista.pop(0))

print(Lista)