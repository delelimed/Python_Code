def linear_search(l, elem):
    for e in l:
        if e == elem: #operazione ripetuta più volte, ripetuta al peggio l volte
            return True
    return False

#posso migliorare quel coso di sopra, se mi trovo in una lista ordinata, in quanto sicuramente sarà il primo elemento

def binary_search(l, elem):
    #base case
    if len(l) == 1:
        if l[0] == elem:
            return True
        else:
            return False
    m = len(l)//2
    if elem == l[m]:
        return True
    #inductive step
    elif elem > l[m]:
        return binary_search(l[m:], elem)
    else:
        return binary_search(l[0:m], elem)


def is_substring(s:str, sub:str):
    #base cases
    if len(s) < len(sub):
        return False
    if s[0:len(sub)] == sub:
        return True
    else:
        return is_substring(s[1:], sub)
        #toglie il primo elemento e chiama la funzione stessa, alla fine arriva ad uno dei due passi base visti sopra

if __name__ == "__main__":
    l = [1,2,3,5,8,9,11,15,17,22,45,67,81,99]
    print("smth")


