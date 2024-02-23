numero_elementi= int(input("Quanti elementi ha la lista? "))

Lista = []
for h in range(numero_elementi):
    elemento=str(input("inserire un elemento "))
    Lista.append(elemento)

verifica = str(input("Di quale elemento vuoi verificare la presenza in lista? "))

if verifica in Lista:
    print("Ci sta")

else:
    print("Che cazzo...")