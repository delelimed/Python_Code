'''
Questo programma prende un numero in ingresso, chiede la base di partenza e lo converte in una base di arrivo.
Come prima cosa converte il numero come intermezzo binario, poi lo converte nella base di destinazione.
'''

Numero1 = str(input("Inserisci il numero INTERO che vuoi convertire: "))
Numero1lista = []
Binstring = []

B1 = int(input("Inserisci la base di partenza: "))
B2 = int(input("Inserisci la base di arrivo: "))
Finale = 0
VOID = None

#inizio la divisione del PRENumero1 nel Numero (LISTA)
tempy = 0
for i in range(len(Numero1)):
    Numero1lista.append(Numero1[tempy])
    tempy += 1
tempy = 1
Numero1 == int(Numero1)
#Verifica della leicità dell'operazione
if any(int(num) > B1 - 1 for num in Numero1lista):
    VOID = True
else:
    VOID = False

if VOID == True:
    print("Attenzione! Il numero inserito o la base di partenza sono errate!")
    quit()
