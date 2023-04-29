'''
Il presente programma chiede in input la lunghezza della lista. In seguito, chiede i singoli elementi della lista, per poi stamparla a schermo, 
invertirla e stamparla nuovamente a schermo (invertita).
'''

NItm = int(input("Da quanti elementi è composta la lista? "))
ItmList = []

for i in range(NItm):
    ITM = int(input("Inserisci il numero: "))
    ItmList.append(ITM)
print("Hai fornito la seguente lista: " + str(ItmList))
ItmList = ItmList[NItm::-1]
print("Di seguito trovi la lista inversa: " + str(ItmList))