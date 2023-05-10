elem = int(input("quanti elementi ci sono nella lista?"))

Lista1= []
Lista2= []

for i in range(elem):
    lett=str(input("inserisci un elemento della prima lista: "))
    Lista1.append(lett)

for i in range(elem):
    num= str(input("inserisci un elemento della seconda lista: "))
    Lista2.append(num)

Comb=[]
Lista1_bak = []
Lista2_bak = []
Lista1_bak = Lista1.copy()
Lista2_bak = Lista2.copy()

for i in range(elem):
    tempy=0
    if tempy==0:
        Comb.append(Lista1.pop(0))
        tempy+=1
    if tempy==1:
        Comb.append(Lista2.pop(0))
        tempy=0
print(Comb)

LungListaComb = int(len(Comb))
LungLista1 = int(len(Lista1_bak))
LungLista2 = int(len(Lista2_bak))

if LungListaComb == LungLista1 + LungLista2:
    print("La lista è corretta")
else:
    print("è successo qualche cazzo e la lista non è corretta")
