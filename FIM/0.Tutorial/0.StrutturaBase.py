
# Definizione Funzioni

def somma(A:int, B:int) -> int:
    '''
    Questa funzione fa la somma tra due numeri
    :param A: prino numero
    :param B: prino numero
    :return ris: risultato
    '''
    ris = A + B
    return ris

def sottrazione(A:int, B:int) -> int:
    return A - B

def moltiplicazione(A:int, B:int) -> int:
    return A * B

def divisione_intera(A:int, B:int) ->int:
    return A//B

def divisione_normale(A:int, B:int) -> float:
    return A / B

def divisione_resto(A:int, B:int) -> int:
    return A % B #restituisce il resto della divisione

def seleziona_divisione(A:int, B:int) -> float:
    sel_div = int(input("Che tipo di divisione vuoi fare? \n"
          "1 - Intera \n"
          "2 - Normale \n"
          "3 - Dammi il resto! \n"
          "Seleziona: "))
    if sel_div == 1:
        Risultato = divisione_intera(A, B)
        print(stampa_ris(Risultato))

    elif sel_div == 2:
        print(stampa_ris(divisione_normale(A, B)))


    elif sel_div == 3:
        print(stampa_ris(divisione_resto(A, B)))


    else:
        print("Hai fatto la cazzata...")
        quit()


def stampa_ris(ris):
    print("Il risultato è: " + str(ris))
    print(f"Il risultato è {ris}")

Num1 = int(input("Inseriscimi un numero: "))
Num2 = int(input("Inseriscimi un altro numero: "))

sel = int(input("Che operazione vuoi fare? \n"
"1 - Addizione \n"
"2 - Sottrazione \n"
"3 - Moltiplicazione \n"
"4 - Una delle tante divisioni \n"
"Seleziona: "))

if sel == 1:
    Peperoni = somma(Num1, Num2)
    print(stampa_ris(Peperoni))

elif sel == 2:
    Peperoni = sottrazione(Num1, Num2)
    print(stampa_ris(Peperoni))

elif sel == 3:
    Peperoni = moltiplicazione(Num1, Num2)
    print(stampa_ris(Peperoni))

elif sel == 4:
    Peperoni = seleziona_divisione(Num1, Num2)

else:
    print("Hai selezionato un valore non valido, ed attualmente non so come dirti che hai fatto una grande cazzata. Riavvia il programma.")

# crea un programma che chieda il nome, cognome, età, corso di studi frequentato e materia preferita tra medicina ed ingegneria (1/2)
#restituisce un testo di presentazione completo [print(f"...")]


