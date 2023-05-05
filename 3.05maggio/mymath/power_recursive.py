def recursive_pow(base, exp):
    if exp == 0:
        return 1
    else:
        return base * recursive_pow(base, exp-1) #ricorsiva perchè chiama sè stessa, importante è che alla fine ne riesca ad uscire

if __name__ == "__main__":
    print(recursive_pow(2,4))

#qua si poteva usare un ciclo for... ma certe volte la ricorsione facilita. se riesco a pensare a come scomporre un problema
#in sottoproblemi e poi come ricomporli la situa è più facile.