'''
algoritmo che trova l'elemento minimo e relativo indice
'''

l = [1,2,3,4,5,0,5]
min = l[0]
min_id = 0
for i in range(len(l)):
    if l[i] < min:
        min = l[i]
        min_id = i
print("Nella lista fornita, il numero minore è " + str(min) + ", avente indirizzo " + str(min_id) + "e posizione nell'elenco " + str(min_id+1))
