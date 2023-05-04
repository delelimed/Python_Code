'''
Questo programma deve chiedere in ingresso due liste ordinate, e restituirne una terza, comunque ordinata.
'''

NItm = int(input("Da quanti elementi è composta ciascuna delle due liste? "))
ItmList1 = []
ItmList2 = []
ItmList3 = []

print("Inserisci, uno per volta, gli elementi della prima lista.")
for i in range(NItm):
    ITM = int(input("Inserisci il numero: "))
    ItmList1.append(ITM)
print("Hai fornito la seguente lista: " + str(ItmList1))
ItmList1 = ItmList1

print("Ora inserisci gli elementi della seconda lista.")
for i in range(NItm):
    ITM = int(input("Inserisci il numero: "))
    ItmList2.append(ITM)
print("Hai fornito la seguente lista: " + str(ItmList2))
ItmList2 = ItmList2

ItmList3 = sorted(ItmList1 + ItmList2)
print("Una nuova lista, ordinata, che combina le due precedenti è la seguente: " + str(ItmList3))