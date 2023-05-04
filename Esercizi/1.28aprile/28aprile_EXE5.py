'''
Chiede in ingresso una una lista di k elementi (richiesti). Poi, chiede quante operazioni di swap eseguire, per mostrare il risultato
a schermo
'''
ItmList = []

NItm = int(input("Da quanti elementi è composta la lista? "))
print("Inserisci, uno per volta, gli elementi della lista: ")
for i in range(NItm):
    ITM = int(input("Inserisci il numero: "))
    ItmList.append(ITM)
print("Hai fornito la seguente lista: " + str(ItmList))

NSWAP = int(input("Di quanti passi vuoi eseguire lo SWAP? "))
for k in range(NSWAP):
    tempy = ItmList.pop(0) #tempy è 5variabile temporanea su cui salvo il numero in corso di swap
    ItmList.append(tempy)
print("La nuova lista di " + str(NItm) + " elementi è la seguente: " + str(ItmList))
