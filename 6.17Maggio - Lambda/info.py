'''
Gestione delle eccezioni. Abbiamo due tipi di errori:
- sintassi, identificati prima che codice venga eseguito (indentazione errata).
- eccezioni, si verificano durante esecuzione del programma. programma termina e stampa nome di eccezioen e stack trace
'''

#Passaggio parametri di una funzione
def foo(a, b):
    return a + b

def foo2(a, increment=1, decrement=1): #posso specificarne anche solo uno, ma devo usare il nome fornito dal programamtore della funzione,
    # e poi non posso assegnare dopo un argomento posizionale, da quel momento in poi devo nominarli tutti
    return a + increment - decrement

print(foo2(1, decrement=1))

# funzioni lambda
# funzioni che non hanno un nome e possono contenere solo una espressione e non possono avere valori di ritorno
L = lambda x, y: x + y

print(L(1,2)) # utile perchè spesso non voglio creare funzioni

lista = [1,2,3,4,4,5,20,8]
# fx filter, applica la funzione a tutti gli elementi, se true lo tiene, altrimenti scarta
a = list(filter(lambda x : x%2 == 0, lista)) #solitamente avrei usato un ciclo
print(a) # altro uso di lambda