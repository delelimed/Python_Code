'''
Questo programma chiede in input il numero di elementi di una lista, seguito dalla lista stessa. Poi, chiede di inserire un numero, per verificare che esso sia presente.
'''

NItm = int(input("Da quanti elementi è composta la lista? "))
ItmList = []

for i in range(NItm):
    ITM = int(input("Inserisci il numero: "))
    ItmList.append(ITM)
print("Hai fornito la seguente lista: " + str(ItmList))

Verifica = int(input("Di quale valore vuoi verificare la presenza nella lista? "))

if Verifica in ItmList:
    print("Il valore " + str(Verifica) + " è presente nella lista")
else:
    print("Il valore " + str(Verifica) + " NON è presente nella lista")
