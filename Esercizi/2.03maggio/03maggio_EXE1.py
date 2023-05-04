'''
Questo programma prende un numero in ingresso, chiede la base di partenza e lo converte in una base di arrivo.
Come prima cosa converte il numero come intermezzo decimale, poi lo converte nella base di destinazione.
Stesso di 27aprile_EXE7, ma con l'implementazione delle funzioni.
'''

def num2dec(Numero, B1) -> str:
    '''
    Questa funzione converte un numero in base 10
    '''
    NumeroDecimale = 0
    tempy = 0
    for i in range(len(Numero)):
        NumeroDecimale += int(Numero[tempy]) * (B1 ** (len(Numero) - 1 - tempy))
        tempy += 1
    return NumeroDecimale

def isnum(show:str) -> int:  #avrebbe senso generare solo questa come funzione, e lasciare le altre come codice?
    '''
    Questa funzione prende un valore in input e verifica che sia un numero: se lo è, lo restituisce, altrimenti chiede di reinserire il valore
    'show' è il messaggio che viene mostrato a schermo
    'N' è il numero che viene restituito
    '''
    N = 0
    while True:
        try:
            N = int(input(show))
            break
        except ValueError:
            print("Te pare un numero?")
    return N


def numconverter(Numero:int, B2:int) -> str:
    '''
    Questa funzione converte un numero da una base decimale ad una base B2
    :param Numero: è il numero decimale da convertire
    :param B2: è la base di arrivo
    :Converted: è il numero convertito
    '''
    Converted = " "
    if B2 == 10:
        Converted = Numero
    else:
        while int(Numero) // B2 or int(Numero) % B2 != 0:
            Converted = str(Converted) + str(int(Numero) % B2)
            Numero = int(Numero) // B2
            Converted = Converted[::-1]
    return Converted

def controlloutil(N:int, B1:int, B2:int) -> bool:
    '''
    Questa funzione controlla che le basi ed il numero inserite siano congrui
    :param N: numero da convertire
    :param B1: base di partenza
    :param B2: base di arrivo
    :return VOID: indica se l'operazione è valida (atteso FALSE)
    '''
    VOID = True #diamo per scontato che l'utente si sia sbagliato
    tempy = 0
    N_List = []
    for i in range(len(N)):
        N_List.append(Numero1[tempy])
        tempy += 1

    if B1 == B2:
        VOID = True
    elif any(int(num) > B1 - 1 for num in N_List):
        VOID = True
    else:
        VOID = False
    return VOID



Numero1 = str(isnum(show="Inserisci il numero INTERO che vuoi convertire: "))
Orig = Numero1
Numero1lista = []
Numero1Decimale = 0
Numero2 = " "

B1 = int(isnum(show="Inserisci la base di partenza: "))
B2 = int(isnum(show="Inserisci la base di arrivo: "))

VOID = controlloutil(Numero1, B1, B2)

if VOID == True:
    print("Attenzione! Il numero inserito o la base di partenza sono errate, oppure la base di partenza coincide con quella di arrivo!")
    quit()


# effettua, come prima cosa, la conversione in base 10
if B1 != 10:
    Numero1Decimale = num2dec(Numero1, B1)

if B1 == 10:
    Numero1Decimale = Orig


print("Il numero " + str(Numero1) + " in base " + str(B1) + " equivale al numero " + str(numconverter(Numero1Decimale, B2)) +
      " convertito in base " + str(B2))
