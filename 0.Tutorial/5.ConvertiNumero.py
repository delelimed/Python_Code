'''
Prendere un numero, una base di partenza ed una di arrivo.
Verificare che la base di partenza sia congrua
Eseguire la conversione
'''

#Dichiaro le funzioni



#Inizio programma

Numero = int(input("Inserisci il numero da convertire: "))
NumeroSTR = str(Numero)


B1 = int(input("Inserisci la base di partenza: "))
B2 = int(input("Inserisi la base di arrivo: "))


NumeroLista = []
tempy = 0
for i in range(len(NumeroSTR)):
    NumeroLista.append(NumeroSTR[tempy])
    tempy +=1
tempy = 1

#verifica della leicità
if any(NumeroSTR) > B1 - 1:
    LECIT = True
else:
    LECIT = False

#Converto, se necessario, il numero di partenza in decimale

NumeroDecimale = 0
NumeroFinale = 0

if B1 != 10:
    NumeroLista = NumeroLista[len(NumeroLista)::-1]
    for i in NumeroLista:
        NumeroDecimale += int(i) * (B1) ** NumeroLista.index(i)
if B1 == 10:
    NumeroDecimale = Numero


# Converto il decimale in destinazione
while int(NumeroDecimale) // B2 or int(NumeroDecimale) % B2 != 0:
    NumeroFinale = str(NumeroFinale)




while int(Numero1Decimale) // B2 or int(Numero1Decimale) % B2 != 0:
    Numero2 = str(Numero2) + str(int(Numero1Decimale) % B2)
    Numero1Decimale = int(Numero1Decimale) // B2


