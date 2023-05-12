# creo una rubrica

from typing import List

class Contatto:
    def __init__(self, nome:str, numero:str):
        self.nome = nome
        self.numero = numero

    def __eq__(self, c):
        return self.nome == c.nome



if __name__ == "__main__":
    Rubrica =[Contatto("mario", "123"),Contatto("mario", "")]

    while True:
        nome = input("Inserisci il nome: ")

        if Contatto(nome, "") in Rubrica:
            i = Rubrica.index(Contatto(nome, ""))
            print(f"Numero: {Rubrica[i].numero}")
        else:
            print("Contatto non trovato")
            prompt = input("Inserirlo? (S/N) ")
            while prompt != "S" and prompt != "N":
                prompt = input("Decidi che cazzo vuoi fare. lo inserisci? ")
            numero = input("Inserisci il numero: ")
            Rubrica.append(Contatto(nome, numero))
