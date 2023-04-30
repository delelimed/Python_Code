'''
Questo programma prende un numero in ingresso, chiede la base di partenza e lo converte in una base di arrivo.
'''

PRENumero = str(input("Inserisci il numero che vuoi convertire: "))
Numero = []
B1 = int(input("Inserisci la base di partenza: "))
B2 = int(input("Inserisci la base di arrivo: "))
Finale = 0
VOID = None

#inizio la divisione del PRENumero nel Numero (LISTA)
tempy = 0
for i in range(len(PRENumero)):
    Numero.append(PRENumero[tempy])
    tempy += 1
tempy = 0
#Verifica della leicità dell'operazione

if any(int(num) > B1 - 1 for num in Numero):
    VOID = True
else:
    VOID = False

if VOID == True:
    print("Attenzione! Il numero inserito o la base di partenza sono errate!")
    quit()
else:
    print("Poi vediamo")


print("Il numero " + str(PRENumero) + " in base " + str(B1) + ", convertito in base " + str(B2) + ", è: " + str(Finale))