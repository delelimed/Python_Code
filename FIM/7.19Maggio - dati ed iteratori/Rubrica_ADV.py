# creo una rubrica

import os
import csv
from typing import List

class Contatto:
    def __init__(self, nome:str, numero:str):
        self.nome = nome
        self.numero = numero

    def read(self, f:str):
        f = f.strip()
        l = f.split(",")
        self.nome = l[0]
        self.numero = l[1]

    def write_line(self, f:str):
        s = f"{self.nome},{self.numero}\n"
        f = s.write(s)




    def __eq__(self, c):
        return self.nome == c.nome



if __name__ == "__main__":

    Rubrica =[]
    if os.path.exists(os.path.join(".", "rubrica.csv")):
        f = open(os.path.join(".","rubrica.csv"), "r", encoding="utf-8")
        for line in f:
            c = Contatto("","")
            c.read(line)
            Rubrica.append(c)
        f.close()

    f = open(os.path.join(".", "rubrica.csv"), "a", encoding="utf-8")




    try:
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
    except KeyboardInterrupt:
        print("salvataggio...")
        f.close()
        quit()