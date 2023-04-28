'''
in questo programma, creiamo una lista con i numeri da 1 a 10, eliminiamo i numeri avente indice compreso
tra due e quattro escluso e lo stampo a schermo (#1).
poi, rigenero la lista completa, la inverto e la stampo nuovamente a schermo (#2).
poi, ci mostra se il numero 3 è presente in a (#3)
ed infine se 11 è presente (#4)
'''

a = [1,2,3,4,5,6,7,8,9,10]
del a[2:4] #1
print(a)
a = [1,2,3,4,5,6,7,8,9,10]
a = a[len(a)-1::-1] #2
print(a)
print(3 in a) #3
print(11 in a) #4