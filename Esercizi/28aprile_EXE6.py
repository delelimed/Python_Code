'''
Chiede di inserire un numero, per poi mostrare a schermo il numero di cifre di cui è composto,
oltre che alle cifre stesse, separate da virgola.
'''

Numero = str(input("Inserisci il numero di cui vuoi conoscere le cifre: "))
Lung = len(Numero)
Lista = []
tempy = 0

for i in range(Lung):
    Lista.append(Numero[tempy])
    tempy +=1
print("Il numero " + str(Numero) + " è composto da " + str(Lung) + " cifre, le quali sono: " + str(Lista))