NItm = int(input("Da quanti elementi è composta ciascuna delle due liste? "))
ItmList1 = []

for i in range(NItm):
    ITM = int(input("Inserisci il numero: "))
    ItmList1.append(ITM)
print("Hai fornito la seguente lista:")
print(ItmList1)

ItmList2 = []

print("Ora inserisci gli elementi della seconda lista.")
for i in range(NItm):
    ITM = int(input("Inserisci il numero: "))
    ItmList2.append(ITM)
print("Hai fornito la seguente lista:")
print(ItmList2)

ItmList3 = []
NItm3 = 2 * NItm
tempy = 0 #controlla il passaggio sincrono tra le due liste ed indexlist
tempyswitch = 1 #se pari lista uno, se dispari lista 2

while tempy <= NItm:
    if tempyswitch % 2 != 0:
        ItmList3.append(ItmList1[tempy])
        tempyswitch += 1
    if tempyswitch % 2 == 0:
        ItmList3.append(ItmList2[tempy])
        tempyswitch = 1
    tempy += 1
if tempy > NItm:
    print("La lista combinata è la seguente: ")
    print(ItmList3)

    
