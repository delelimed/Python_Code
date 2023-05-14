# Definizione di funzioni
def isnum(show:str) -> int:
    '''
    Questa funzione prende in input il numero inserito dall'utente e lo restituisce al programma.
    In caso di errore (se non ottiene un numero), chiede nuovamente di inserire un numero.
    :param show: Testo da mostrare all'utente
    :return: numero
    '''
    N = 0
    while True:
        try:
            N = int(input(show))
            break
        except ValueError:
            print("Te pare un numero?")
    return N

def controlloutil(N:int, Bpar:int, Barr:int) -> bool:
    '''
    Prende in ingresso i tre valori definiti dall'utente e controlla che: la base di partenza sia congrua con il numero
    e che la base di partenza sia diversa da quella di arrivo.
    :param N: numero da convertire
    :param Bpar: base di partenza
    :param Barr: base di arrivo
    :return VOID: indica se l'operazione è INVALIDA (atteso FALSE)
    '''
    VOID = True #prendiamo per scontato che l'utente si sia sbagliato
    counter = 0
    N_List = []
    for i in range(len(N)):
        N_List.append(N[counter])
        counter += 1

    #verifichiamo che le basi di partenza siano diverse
    if Bpar == Barr:
        VOID = True
    elif any(int(cifra) > Bpar - 1 for cifra in N_List):
        VOID = True
    else:
        VOID = False
    return VOID

def num2dec(N:int, Bpar:int) -> str:
    '''
    Questa funzione converte un numero in decimale
    :param N: numero da convertire
    :param Bpar: base di partenza
    :return: numero convertito
    '''
    NumeroDecimale = 0
    counter = 0
    for cifra in range(len(N)):
        NumeroDecimale += int(N[counter]) * (Bpar **(len(N) - 1 - counter))
        counter += 1
    return NumeroDecimale

def numconverter(Ndec:int, B2:int) -> str:
    '''
    Questa funzione converte un numero da una base decimale ad una base B2
    :param Ndec: numero DECIMALE
    :param B2: base di arrivo
    :return: numero convertito
    '''
    converted = ""
    if B2 == 10:
        converted = Ndec
    else:
        while int(Ndec) // B2 or int(Ndec) % B2 != 0:
            converted = str(converted) + str(int(Ndec) % B2)
            Ndec = int(Ndec) // B2
        converted = converted[::-1]
    return converted


# Programma effettivo
if __name__ == "__main__":
    #Fase di input da utente. Attesa dati.
    Numero1 = str(isnum("Inserisci il numero intero che vuoi convertire: "))
    Orig = Numero1
    B1 = isnum("Inserisci la base di partenza: ")
    B2 = isnum("Inserisci la base di arrivo: ")

    #verifica della leicità
    INVALID = controlloutil(Numero1, B1, B2)
    if INVALID == True:
        print("Attenzione! Il numero inserito o la base di partenza è errato, oppure la base di partenza coincide con quella di arrivo!")
        quit()

    #effettuare la conversione in base 10, se necessaria
    if B1 != 10:
        Numero1Decimale = num2dec(Numero1, B1)
    elif B1 == 10:
        Numero1Decimale = Orig

    #effettuo la conversione vera e propria
    NumeroFinale = numconverter(Numero1Decimale, B2)

    #mostro a schermo il risultato
    print(f"Il numero {Orig} in base {B1} equivale al numero {NumeroFinale} in base {B2}")
