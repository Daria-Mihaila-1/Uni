def prim(p):
    if p > 1:
        if ( p == 2 ) or ( p == 3 ):
            return(True)
        else:
            pri = True
            for t in range(2, int( p**(1/2)+1 )):
                if p % t == 0:
                    pri = False
                    break
            return(pri)

def twinziess(n):
    p = 3
    q = p + 2
    nr = 1
    print(p,' ',q)
    while nr < n:
        p += 2
        q = p + 2
        if prim(p) and prim(q):
            print(p,' ',q,' ')
            nr += 1

def langste_abnehmende_teilfolge(lst):
    """
    die Funktion gibt die langste abnehmende aufeinanderfolgende Teilfolge aus einer Liste lst zuruck
     input Parameter:die Liste lst
    lmax: die lange der langsten abnehmenden aufeinanderfolgenden Teilfolge
    stanga: die Position des ersten Elementes der Teilfolge
    dreapta: die Position des letzten Elementes der Teilfolge
    l: die Lange einer abnehmender aufeinanderfolgenden Teilfolge
    st:die erste Position der Teilfolge der Lange l
    dr:die letzte Position der Teilfolge der Lange l
    i: Kontorvariable fur die Liste
    """
    lmax = 1
    stanga = -1
    dreapta = -1
    l = 1
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            if l == 1:
                st = i
            dr = i + 1
            l += 1
        else:
            l = 1
        if l > lmax:
                lmax = l
                dreapta = dr
                stanga = st

    print(lst[stanga:dreapta+1])

def main():
    n = int(input('n-'))
    twinziess(n)
    lst = [1, 2, 3, 5, 2, 3, 4, 9, 8, 7, 6]
    langste_abnehmende_teilfolge(lst)

main()
               


