def foo1(l:list[int]):
    for i in range(len(l)):
        l[i] = 1
def foo2(l:list[int]):
    l = [2,2,2]
def foo3(l:list[int]):
    l = l.copy()
    for i in range(len(l)):
        l[i] = 3
    return l
if __name__=="__main__":
    l = [1,2,3]
    foo1(l)
    print(l)
    foo2(l)
    print(l)
    l3 = foo3(l)
    print(l)
    print(l3)
