'''
unisce tipo di dato o concetto, che racchiude dati e funzionalità
classe di crea con class NomeClasse, posso mettere una stringa che descrive cosa è la mia classe (docs)

Se voglio creare attributi diversi ma gli stessi per ogni cittadino, devo ridefinire __init__(1)

Differenza tra metodo e funzione: metodo è funzione che viene chiamata da oggetto, se chiamo la funzione, la chiamo senza
argomenti
anche operatori sono metodi di oggetto
'''

#(1)
def __init__(self,id):
    self.id = id

class Example:
    def __init__(self, id):
        self.id = id
    def stampa(self):
        print(self.id)

Example.stampa(4)
e = Example(1)