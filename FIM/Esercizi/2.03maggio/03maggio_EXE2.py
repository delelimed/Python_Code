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

def numpotenza(N:int, P:int) -> int:
    '''
    Questa funzione eleva un numero alla potenza
    :param N: numero da elevare
    :param P: potenza a cui elevare il numero
    :return NP: numero elevato alla potenza
    '''
    for i in range(P):
        NP = N * N
    return NP

#-----INIZIO DEL SOFTWARE-----
Numero = int(isnum("Inserisci il numero che vuoi elevare a potenza: "))
Potenza = int(isnum("Inserisci la potenza a cui vuoi elevare il numero: "))

print("Il numero", Numero, "elevato alla potenza", Potenza, "è:", numpotenza(Numero, Potenza))